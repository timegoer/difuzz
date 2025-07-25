import os
import random
import shlex
import shutil
import subprocess
import time

from config import (
    CC,
    DIFF_SO_PATH,
    ELF2HEX,
    EMU_BINARY,
    FUZZ_EMU,
    NEMU_BINARY,
    OBJCOPY,
    NEMU_TIMEOUT,
    NUM_ITER,
)
from mutator import rvMutator, simInput
from preprocessor import rvPreProcessor


def save_mismatch(
    base, proc_num, out, sim_input: simInput, data: list, num, generator_name="id_"
):  # , elf, asm, hexfile, mNum):
    sim_input.save(out + "/sim_input/{}_{}.si".format(generator_name, num), data)

    elf = base + "/.input_{}.elf".format(proc_num)
    asm = base + "/.input_{}.S".format(proc_num)
    hexfile = base + "/.input_{}.hex".format(proc_num)
    bin = base + "/.input_{}.bin".format(proc_num)
    try:
        shutil.copy(elf, out + "/elf/{}_{}.elf".format(generator_name, num))
        shutil.copy(bin, out + "/bin/{}_{}.bin".format(generator_name, num))
        shutil.copy(asm, out + "/asm/{}_{}.S".format(generator_name, num))
        shutil.copy(hexfile, out + "/hex/{}_{}.hex".format(generator_name, num))
    except FileNotFoundError:
        pass


def run_nemu_test(proc_num: int, output_dir: str) -> int:
    """执行NEMU测试并返回状态码"""
    input_file = f"{output_dir}/.input_{proc_num}.bin"
    cmd = shlex.split(f"{NEMU_BINARY} -b {input_file}")

    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=NEMU_TIMEOUT,
            check=True,
        )
        return result.returncode
    except subprocess.TimeoutExpired:
        print("NEMU timeout")
        return -1  # 超时状态码
    except subprocess.CalledProcessError as e:
        print(f"NEMU fail returncode: {e.returncode}")
        return e.returncode


# TODO
# spike 和 nemu 软件覆盖引导
def main():
    num_iter = NUM_ITER
    out = "output"
    template = "Template"
    if not os.path.isdir(out):
        os.makedirs(out)
    if not os.path.isdir(out + "/corpus"):
        os.makedirs(out + "/corpus")
        os.makedirs(out + "/corpus/sim_input")
        os.makedirs(out + "/corpus/elf")
        os.makedirs(out + "/corpus/asm")
        os.makedirs(out + "/corpus/hex")
        os.makedirs(out + "/corpus/bin")
    if (FUZZ_EMU == 1) and (not os.path.isdir(out + "/emu_mismatch")):
        os.makedirs(out + "/emu_mismatch")
        os.makedirs(out + "/emu_mismatch/sim_input")
        os.makedirs(out + "/emu_mismatch/elf")
        os.makedirs(out + "/emu_mismatch/asm")
        os.makedirs(out + "/emu_mismatch/hex")
        os.makedirs(out + "/emu_mismatch/bin")
    random.seed(time.time())
    mutator = rvMutator(no_guide=0)
    preprocessor = rvPreProcessor(CC, ELF2HEX, OBJCOPY, template, out, 0)
    coverage_count = 0
    while num_iter > 0:
        sim_input, data, generator_name = mutator.get()
        symbols, version = preprocessor.process(sim_input, data, False)
        nemu_ret = run_nemu_test(0, out)
        if nemu_ret == 0:
            print(f"[DifuzzNEMU] iter [{coverage_count}] PASS")
            save_mismatch(
                out,
                0,
                f"{out}/corpus",
                sim_input,
                data,
                coverage_count,
                generator_name,
            )
            mutator.add_corpus(sim_input)
            coverage_count += 1
            num_iter -= 1
            if FUZZ_EMU == 1:
                input_bin = f"{out}/.input_0.bin"
                emu_ret = subprocess.call(
                    [EMU_BINARY, "--diff", DIFF_SO_PATH, "-i", input_bin],
                    stderr=subprocess.DEVNULL,
                )
                if emu_ret != 0:
                    print(f"[DifuzzEMU] iter [{coverage_count}] FAIL")
                    save_mismatch(
                        out,
                        0,
                        f"{out}/emu_mismatch",
                        sim_input,
                        data,
                        coverage_count,
                        generator_name,
                    )
                else:
                    print(f"[DifuzzEMU] iter [{coverage_count}] PASS")


if __name__ == "__main__":
    main()
