# difuzz

# Install elf2hex
git clone https://github.com/sifive/elf2hex.git
pushd elf2hex > /dev/null
autoreconf -i
./configure --target=riscv64-unknown-elf
make

把对应的路径写入config.py，然后直接运行
`python3 Fuzzer.py`
即可
