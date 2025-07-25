CC = "/nfs/home/changgen/local/bin/riscv64-unknown-linux-gnu-gcc"
CC_ARCH = "-march=rv64gcvh_zicbop_zicbom_zicboz"
# CC_ARCH = "-march=rv64gcv"
ELF2HEX = "/nfs/home/changgen/local/bin/riscv64-unknown-elf-elf2hex"
OBJCOPY = "/nfs/home/changgen/local/bin/riscv64-unknown-linux-gnu-objcopy"
# SPIKE = "/nfs/home/changgen/riscv-isa-sim/build/spike"
# SPIKE_ISA_ARG = "--isa=rv64imafdcvh_zicntr_zihpm_zicbom_zicboz_zicbop"

FUZZ_EMU = 0
EMU_BINARY = "/nfs/home/changgen/xs-env/XiangShan/build/emu"
DIFF_SO_PATH = "/nfs/home/changgen/xs-env/NEMU/ready-to-run/riscv64-nemu-interpreter-so"

Fuzz_NEMU = 1
NEMU_BINARY = "/nfs/home/changgen/xs-env/NEMU/build/riscv64-nemu-interpreter"
NEMU_TIMEOUT = 1  # 秒

NUM_ITER = 3000
CORPUS_SIZE = 300
NUM_PREFIX = 0
NUM_WORDS = 100
NUM_SUFFIX = 0

# 把希望生成的类型设置为1即可
GENERATOR_SELECTOR = [
    0,  # CounterTimerGenerator("RV64G"),
    0,  # ExceptionGenerator("RV64G"),
    0,  # InterruptGenerator("RV64G"),
    0,  # RandSwitchGenerator("RV64G"),
    0,  # RandomInstGenerator("RV64G"),
    0,  # IllLow2highGenerator("RV64G"),
    0,  # M2SLegalSwitchGenerator("RV64G"),
    0,  # S2ULegalSwitchGenerator("RV64G"),
    0,  # HyperviserGenerator("RV64G"),
    1,  # BitmaprGenerator("RV64G"),
    0,  # MptGenerator("RV64G"),
    0,  # CBOGenerator("RV64G"),
    0,  # TODO VectorGenerator
]
