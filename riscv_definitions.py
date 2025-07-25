"""RISCV Opcodes"""

NONE = -1
USER = 0
SUPERVISOR = 1
HYPERVISOR = 2
MACHINE = 3

prv = {
    NONE: "None",
    USER: "User",
    SUPERVISOR: "Supervisor",
    HYPERVISOR: "Hypervisor",
    MACHINE: "Machine",
}
# Memory operations should access limited size of regions
#
rv32i_rtype = {
    # opcode: (syntax, xregs, fregs, imms, symbols)
    "add": (
        "add xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "sub": (
        "sub xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "sll": (
        "sll xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "slt": (
        "slt xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "sltu": (
        "sltu xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "xor": (
        "xor xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "srl": (
        "srl xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "sra": (
        "sra xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "or": (
        "or xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "and": (
        "and xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
}

rv32i_itype = {
    "jalr": (
        "jalr xreg0, 0(xreg1)",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (),
        (),
    ),
    "lb": (
        "lb xreg0, imm6(xreg1)",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("imm6", 1),),
        (),
    ),
    "lh": (
        "lh xreg0, imm6(xreg1)",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("imm6", 2),),
        (),
    ),
    "lw": (
        "lw xreg0, imm6(xreg1)",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("imm6", 4),),
        (),
    ),
    "lbu": (
        "lbu xreg0, imm6(xreg1)",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("imm6", 1),),
        (),
    ),
    "lhu": (
        "lhu xreg0, imm6(xreg1)",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("imm6", 2),),
        (),
    ),
    "slli": (
        "slli xreg0, xreg1, uimm5",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("uimm5", 1),),
        (),
    ),
    "srli": (
        "srli xreg0, xreg1, uimm5",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("uimm5", 1),),
        (),
    ),
    "srai": (
        "srai xreg0, xreg1, uimm5",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("uimm5", 1),),
        (),
    ),
    "addi": (
        "addi xreg0, xreg1, imm12",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("imm12", 1),),
        (),
    ),
    "slti": (
        "slti xreg0, xreg1, imm12",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("imm12", 1),),
        (),
    ),
    "sltiu": (
        "sltiu xreg0, xreg1, imm12",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("imm12", 1),),
        (),
    ),
    "xori": (
        "xori xreg0, xreg1, imm12",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("imm12", 1),),
        (),
    ),
    "ori": (
        "ori xreg0, xreg1, imm12",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("imm12", 1),),
        (),
    ),
    "andi": (
        "andi xreg0, xreg1, imm12",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("imm12", 1),),
        (),
    ),
    "fence": ("fence", (), (), (), ()),
    "ecall": ("ecall", (), (), (), ()),
    "ebreak": ("ebreak", (), (), (), ()),
}

rv32i_stype = {
    "sb": (
        "sb xreg0, imm6(xreg1)",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("imm6", 1),),
        (),
    ),
    "sh": (
        "sh xreg0, imm6(xreg1)",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("imm6", 2),),
        (),
    ),
    "sw": (
        "sw xreg0, imm6(xreg1)",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("imm6", 4),),
        (),
    ),
}

rv32i_btype = {
    "beq": (
        "beq xreg0, xreg1, symbol",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (),
        ("symbol",),
    ),
    "bne": (
        "bne xreg0, xreg1, symbol",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (),
        ("symbol",),
    ),
    "blt": (
        "blt xreg0, xreg1, symbol",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (),
        ("symbol",),
    ),
    "bge": (
        "bge xreg0, xreg1, symbol",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (),
        ("symbol",),
    ),
    "bltu": (
        "bltu xreg0, xreg1, symbol",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (),
        ("symbol",),
    ),
    "bgeu": (
        "bgeu xreg0, xreg1, symbol",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (),
        ("symbol",),
    ),
}

rv32i_utype = {
    "lui": ("lui xreg0, uimm20", ("xreg0",), (), (("uimm20", 1),), ()),
    "auipc": ("auipc xreg0, uimm20", ("xreg0",), (), (("uimm20", 1),), ()),
}

rv32i_jtype = {"jal": ("jal xreg0, symbol", ("xreg0",), (), (), ("symbol",))}

rv32i_rtype = {
    "addw": (
        "addw xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "subw": (
        "subw xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "sllw": (
        "sllw xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "srlw": (
        "srlw xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "sraw": (
        "sraw xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
}

rv64i_itype = {
    "lwu": (
        "lwu xreg0, imm6(xreg1)",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("imm6", 4),),
        (),
    ),
    "ld": (
        "ld xreg0, imm6(xreg1)",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("imm6", 8),),
        (),
    ),
    "slli": (
        "slli xreg0, xreg1, uimm6",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("uimm6", 1),),
        (),
    ),
    "srli": (
        "srli xreg0, xreg1, uimm6",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("uimm6", 1),),
        (),
    ),
    "srai": (
        "srai xreg0, xreg1, uimm6",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("uimm6", 1),),
        (),
    ),
    "addiw": (
        "addiw xreg0, xreg1, imm12",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("imm12", 1),),
        (),
    ),
    "slliw": (
        "slliw xreg0, xreg1, uimm5",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("uimm5", 1),),
        (),
    ),
    "srliw": (
        "srliw xreg0, xreg1, uimm5",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("uimm5", 1),),
        (),
    ),
    "sraiw": (
        "sraiw xreg0, xreg1, uimm5",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("uimm5", 1),),
        (),
    ),
}

rv64i_stype = {
    "sd": (
        "sd xreg0, imm6(xreg1)",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (("imm6", 8),),
        (),
    )
}

rv_zifencei = {
    "fence.i": ("fence.i", (), (), (), ()),
    "sfence.vma": (
        "sfence.vma xreg0, xreg1",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (),
        (),
    ),
}

rv_zicsr = {
    "csrrw": (
        "csrrw xreg0, {}, xreg1",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (),
        (),
    ),
    "csrrs": (
        "csrrs xreg0, {}, xreg1",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (),
        (),
    ),
    "csrrc": (
        "csrrc xreg0, {}, xreg1",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (),
        (),
    ),
    "csrrwi": ("csrrwi xreg0, {}, uimm5", ("xreg0",), (), (("uimm5", 1),), ()),
    "csrrsi": ("csrrsi xreg0, {}, uimm5", ("xreg0",), (), (("uimm5", 1),), ()),
    "csrrci": ("csrrci xreg0, {}, uimm5", ("xreg0",), (), (("uimm5", 1),), ()),
}

rv32m_rtype = {
    "mul": (
        "mul xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "mulh": (
        "mulh xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "mulhsu": (
        "mulhsu xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "mulhu": (
        "mulhu xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "div": (
        "div xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "divu": (
        "divu xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "rem": (
        "rem xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "remu": (
        "remu xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
}

rv64m_rtype = {
    "mulw": (
        "mulw xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "divw": (
        "divw xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "divuw": (
        "divuw xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "remw": (
        "remw xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "remuw": (
        "remuw xreg0, xreg1, xreg2",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
}

rv32a_rtype = {
    "lr.w": (
        "lr.w xreg0, (xreg1)",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (),
        (),
    ),
    "sc.w": (
        "sc.w xreg0, xreg2, (xreg1)",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "amoswap.w": (
        "amoswap.w xreg0, xreg2, (xreg1)",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "amoadd.w": (
        "amoadd.w xreg0, xreg2, (xreg1)",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "amoxor.w": (
        "amoxor.w xreg0, xreg2, (xreg1)",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "amoand.w": (
        "amoand.w xreg0, xreg2, (xreg1)",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "amoor.w": (
        "amoor.w xreg0, xreg2, (xreg1)",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "amomin.w": (
        "amomin.w xreg0, xreg2, (xreg1)",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "amomax.w": (
        "amomax.w xreg0, xreg2, (xreg1)",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "amominu.w": (
        "amominu.w xreg0, xreg2, (xreg1)",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "amomaxu.w": (
        "amomaxu.w xreg0, xreg2, (xreg1)",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
}

rv64a_rtype = {
    "lr.d": (
        "lr.d xreg0, (xreg1)",
        (
            "xreg0",
            "xreg1",
        ),
        (),
        (),
        (),
    ),
    "sc.d": (
        "sc.d xreg0, xreg1, (xreg1)",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "amoswap.d": (
        "amoswap.d xreg0, xreg2, (xreg1)",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "amoadd.d": (
        "amoadd.d xreg0, xreg2, (xreg1)",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "amoxor.d": (
        "amoxor.d xreg0, xreg2, (xreg1)",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "amoand.d": (
        "amoand.d xreg0, xreg2, (xreg1)",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "amoor.d": (
        "amoor.d xreg0, xreg2, (xreg1)",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "amomin.d": (
        "amomin.d xreg0, xreg2, (xreg1)",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "amomax.d": (
        "amomax.d xreg0, xreg2, (xreg1)",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "amominu.d": (
        "amominu.d xreg0, xreg2, (xreg1)",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
    "amomaxu.d": (
        "amomaxu.d xreg0, xreg2, (xreg1)",
        (
            "xreg0",
            "xreg1",
            "xreg2",
        ),
        (),
        (),
        (),
    ),
}

rv32f_rtype = {
    "fadd.s": (
        "fadd.s freg0, freg1, freg2, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),
    "fsub.s": (
        "fsub.s freg0, freg1, freg2, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),
    "fmul.s": (
        "fmul.s freg0, freg1, freg2, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),
    "fdiv.s": (
        "fdiv.s freg0, freg1, freg2, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),
    "fsqrt.s": (
        "fsqrt.s freg0, freg1, {}",
        (),
        (
            "freg0",
            "freg1",
        ),
        (),
        (),
    ),
    "fsgnj.s": (
        "fsgnj.s freg0, freg1, freg2",
        ("xreg0",),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),  # rm: J(N,)/JX
    "fsgnjn.s": (
        "fsgnjn.s freg0, freg1, freg2",
        ("xreg0",),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),  # rm: J(N,)/JX
    "fsgnjx.s": (
        "fsgnjx.s freg0, freg1, freg2",
        ("xreg0",),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),  # rm: J(N,)/JX
    "fmin.s": (
        "fmin.s freg0, freg1, freg2",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),  # rm: MIN/MAX
    "fmax.s": (
        "fmax.s freg0, freg1, freg2",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),  # rm: MIN/MAX
    "fcvt.w.s": ("fcvt.w.s xreg0, freg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fcvt.wu.s": ("fcvt.wu.s xreg0, freg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fmv.x.w": ("fmv.x.w xreg0, freg0", ("xreg0",), ("freg0",), (), ()),
    "feq.s": (
        "feq.s xreg0, freg0, freg1",
        ("xreg0",),
        (
            "freg0",
            "freg1",
        ),
        (),
        (),
    ),
    "flt.s": (
        "flt.s xreg0, freg0, freg1",
        ("xreg0",),
        (
            "freg0",
            "freg1",
        ),
        (),
        (),
    ),
    "fle.s": (
        "fle.s xreg0, freg0, freg1",
        ("xreg0",),
        (
            "freg0",
            "freg1",
        ),
        (),
        (),
    ),
    "fclass.s": ("fclass.s xreg0, freg0", ("xreg0",), ("freg0",), (), ()),
    "fcvt.s.w": ("fcvt.s.w freg0, xreg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fcvt.s.wu": ("fcvt.s.wu freg0, xreg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fmv.w.x": ("fmv.w.x freg0, xreg0", ("xreg0",), ("freg0",), (), ()),
}

rv32f_r4type = {
    "fmadd.s": (
        "fmadd.s freg0, freg1, freg2, freg3, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
            "freg3",
        ),
        (),
        (),
    ),
    "fmsub.s": (
        "fmsub.s freg0, freg1, freg2, freg3, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
            "freg3",
        ),
        (),
        (),
    ),
    "fnmsub.s": (
        "fnmsub.s freg0, freg1, freg2, freg3, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
            "freg3",
        ),
        (),
        (),
    ),
    "fnmadd.s": (
        "fnmadd.s freg0, freg1, freg2, freg3, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
            "freg3",
        ),
        (),
        (),
    ),
}

rv32f_itype = {
    "flw": ("flw freg0, imm6(xreg1)", ("xreg1",), ("freg0",), (("imm6", 4),), ())
}

rv32f_stype = {
    "fsw": ("fsw freg0, imm6(xreg1)", ("xreg1",), ("freg0",), (("imm6", 4),), ())
}

rv64f_rtype = {
    "fcvt.l.s": ("fcvt.l.s xreg0, freg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fcvt.lu.s": ("fcvt.lu.s xreg0, freg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fcvt.s.l": ("fcvt.s.l freg0, xreg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fcvt.s.lu": ("fcvt.s.lu freg0, xreg0, {}", ("xreg0",), ("freg0",), (), ()),
}

rv32d_rtype = {
    "fadd.d": (
        "fadd.d freg0, freg1, freg2, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),
    "fsub.d": (
        "fsub.d freg0, freg1, freg2, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),
    "fmul.d": (
        "fmul.d freg0, freg1, freg2, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),
    "fdiv.d": (
        "fdiv.d freg0, freg1, freg2, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),
    "fsqrt.d": (
        "fsqrt.d freg0, freg1, {}",
        (),
        (
            "freg0",
            "freg1",
        ),
        (),
        (),
    ),
    "fsgnj.d": (
        "fsgnj.d freg0, freg1, freg2",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),  # rm: J(N,)/JX
    "fsgnjn.d": (
        "fsgnjn.d freg0, freg1, freg2",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),  # rm: J(N,)/JX
    "fsgnjx.d": (
        "fsgnjx.d freg0, freg1, freg2",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),  # rm: J(N,)/JX
    "fmin.d": (
        "fmin.d freg0, freg1, freg2",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),  # rm: MIN/MAX
    "fmax.d": (
        "fmax.d freg0, freg1, freg2",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),  # rm: MIN/MAX
    "fcvt.d.s": (
        "fcvt.d.s freg0, freg0, {}",
        (),
        (
            "freg0",
            "freg1",
        ),
        (),
        (),
    ),
    "fcvt.s.d": (
        "fcvt.s.d freg0, freg0, {}",
        (),
        (
            "freg0",
            "freg1",
        ),
        (),
        (),
    ),
    "feq.d": (
        "feq.d xreg0, freg0, freg1",
        ("xreg0",),
        (
            "freg0",
            "freg1",
        ),
        (),
        (),
    ),
    "flt.d": (
        "flt.d xreg0, freg0, freg1",
        ("xreg0",),
        (
            "freg0",
            "freg1",
        ),
        (),
        (),
    ),
    "fle.d": (
        "fle.d xreg0, freg0, freg1",
        ("xreg0",),
        (
            "freg0",
            "freg1",
        ),
        (),
        (),
    ),
    "fclass.d": ("fclass.d xreg0, freg0", ("xreg0",), ("freg0",), (), ()),
    "fcvt.w.d": ("fcvt.w.d xreg0, freg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fcvt.wu.d": ("fcvt.wu.d xreg0, freg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fcvt.d.w": ("fcvt.d.w freg0, xreg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fcvt.d.wu": ("fcvt.d.wu freg0, xreg0, {}", ("xreg0",), ("freg0",), (), ()),
}

rv32d_r4type = {
    "fmadd.d": (
        "fmadd.d freg0, freg1, freg2, freg3, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
            "freg3",
        ),
        (),
        (),
    ),
    "fmsub.d": (
        "fmsub.d freg0, freg1, freg2, freg3, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
            "freg3",
        ),
        (),
        (),
    ),
    "fnmsub.d": (
        "fnmsub.d freg0, freg1, freg2, freg3, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
            "freg3",
        ),
        (),
        (),
    ),
    "fnmadd.d": (
        "fnmadd.d freg0, freg1, freg2, freg3, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
            "freg3",
        ),
        (),
        (),
    ),
}

rv32d_itype = {
    "fld": ("fld freg0, imm6(xreg1)", ("xreg1",), ("freg0",), (("imm6", 4),), ())
}

rv32d_stype = {
    "fsd": ("fsd freg0, imm6(xreg1)", ("xreg1",), ("freg0",), (("imm6", 4),), ())
}

rv64d_rtype = {
    "fcvt.l.d": ("fcvt.l.d xreg0, freg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fcvt.lu.d": ("fcvt.lu.d xreg0, freg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fmv.x.d": ("fmv.x.d xreg0, freg0", ("xreg0",), ("freg0",), (), ()),
    "fcvt.d.l": ("fcvt.d.l freg0, xreg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fcvt.d.lu": ("fcvt.d.lu freg0, xreg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fmv.d.x": ("fmv.d.x freg0, xreg0", ("xreg0",), ("freg0",), (), ()),
}

rv32q_rtype = {
    "fadd.q": (
        "fadd.q freg0, freg1, freg2, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),
    "fsub.q": (
        "fsub.q freg0, freg1, freg2, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),
    "fmul.q": (
        "fmul.q freg0, freg1, freg2, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),
    "fdiv.q": (
        "fdiv.q freg0, freg1, freg2, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),
    "fsqrt.q": (
        "fsqrt.q freg0, freg1, {}",
        (),
        (
            "freg0",
            "freg1",
        ),
        (),
        (),
    ),
    "fsgnj.q": (
        "fsgnj.q freg0, freg1, freg2",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),  # rm: J(N,)/JX
    "fsgnjn.q": (
        "fsgnjn.q freg0, freg1, freg2",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),  # rm: J(N,)/JX
    "fsgnjx.q": (
        "fsgnjx.q freg0, freg1, freg2",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),  # rm: J(N,)/JX
    "fmin.q": (
        "fmin.q freg0, freg1, freg2",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),  # rm: MIN/MAX
    "fmax.q": (
        "fmax.q freg0, freg1, freg2",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
        ),
        (),
        (),
    ),  # rm: MIN/MAX
    "fcvt.q.s": (
        "fcvt.q.s freg0, freg0, {}",
        (),
        (
            "freg0",
            "freg1",
        ),
        (),
        (),
    ),
    "fcvt.s.q": (
        "fcvt.s.q freg0, freg0, {}",
        (),
        (
            "freg0",
            "freg1",
        ),
        (),
        (),
    ),
    "fcvt.q.d": (
        "fcvt.q.d freg0, freg0, {}",
        (),
        (
            "freg0",
            "freg1",
        ),
        (),
        (),
    ),
    "fcvt.d.q": (
        "fcvt.d.q freg0, freg0, {}",
        (),
        (
            "freg0",
            "freg1",
        ),
        (),
        (),
    ),
    "feq.q": (
        "feq.q xreg0, freg0, freg1",
        ("xreg0",),
        (
            "freg0",
            "freg1",
        ),
        (),
        (),
    ),
    "flt.q": (
        "flt.q xreg0, freg0, freg1",
        ("xreg0",),
        (
            "freg0",
            "freg1",
        ),
        (),
        (),
    ),
    "fle.q": (
        "fle.q xreg0, freg0, freg1",
        ("xreg0",),
        (
            "freg0",
            "freg1",
        ),
        (),
        (),
    ),
    "fclass.q": ("fclass.q xreg0, freg0", ("xreg0",), ("freg0",), (), ()),
    "fcvt.wu.q": ("fcvt.wu.q xreg0, freg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fcvt.w.q": ("fcvt.w.q xreg0, freg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fcvt.q.w": ("fcvt.q.w freg0, xreg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fcvt.q.wu": ("fcvt.q.wu freg0, xreg0, {}", ("xreg0",), ("freg0",), (), ()),
}

rv32q_r4type = {
    "fmadd.q": (
        "fmadd.q freg0, freg1, freg2, freg3, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
            "freg3",
        ),
        (),
        (),
    ),
    "fmsub.q": (
        "fmsub.q freg0, freg1, freg2, freg3, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
            "freg3",
        ),
        (),
        (),
    ),
    "fnmsub.q": (
        "fnmsub.q freg0, freg1, freg2, freg3, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
            "freg3",
        ),
        (),
        (),
    ),
    "fnmadd.q": (
        "fnmadd.q freg0, freg1, freg2, freg3, {}",
        (),
        (
            "freg0",
            "freg1",
            "freg2",
            "freg3",
        ),
        (),
        (),
    ),
}

rv32q_itype = {
    "flq": ("flq freg0, imm6(xreg1)", ("xreg1",), ("freg0",), (("imm6", 4),), ())
}

rv32q_stype = {
    "fsq": ("fsq freg0, imm6(xreg1)", ("xreg1",), ("freg0",), (("imm6", 4),), ())
}

rv64q_rtype = {
    "fcvt.l.q": ("fcvt.l.q xreg0, freg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fcvt.lu.q": ("fcvt.lu.q xreg0, freg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fmv.x.q": ("fmv.x.q xreg0, freg0", ("xreg0",), ("freg0",), (), ()),
    "fcvt.q.l": ("fcvt.q.l freg0, xreg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fcvt.q.lu": ("fcvt.q.lu freg0, xreg0, {}", ("xreg0",), ("freg0",), (), ()),
    "fmv.q.x": ("fmv.q.x freg0, xreg0", ("xreg0",), ("freg0",), (), ()),
}

hv_instructions = {
    # Hypervisor内存屏障指令
    "hfence.vvma": ("hfence.vvma xreg0, xreg1", ("xreg0", "xreg1"), (), (), ()),
    "hfence.gvma": ("hfence.gvma xreg0, xreg1", ("xreg0", "xreg1"), (), (), ()),
    # Hypervisor加载指令
    "hlv.b": ("hlv.b xreg0, (xreg1)", ("xreg0", "xreg1"), (), (), ()),
    "hlv.bu": ("hlv.bu xreg0, (xreg1)", ("xreg0", "xreg1"), (), (), ()),
    "hlv.h": ("hlv.h xreg0, (xreg1)", ("xreg0", "xreg1"), (), (), ()),
    "hlv.hu": ("hlv.hu xreg0, (xreg1)", ("xreg0", "xreg1"), (), (), ()),
    "hlv.w": ("hlv.w xreg0, (xreg1)", ("xreg0", "xreg1"), (), (), ()),
    "hlv.d": ("hlv.d xreg0, (xreg1)", ("xreg0", "xreg1"), (), (), ()),
    "hlvx.wu": ("hlvx.wu xreg0, (xreg1)", ("xreg0", "xreg1"), (), (), ()),
    "hlvx.hu": ("hlvx.hu xreg0, (xreg1)", ("xreg0", "xreg1"), (), (), ()),
    # Hypervisor存储指令
    "hsv.b": ("hsv.b xreg0, (xreg1)", ("xreg0", "xreg1"), (), (), ()),
    "hsv.h": ("hsv.h xreg0, (xreg1)", ("xreg0", "xreg1"), (), (), ()),
    "hsv.d": ("hsv.d xreg0, (xreg1)", ("xreg0", "xreg1"), (), (), ()),
    "hsv.w": ("hsv.w xreg0, (xreg1)", ("xreg0", "xreg1"), (), (), ()),
    # "hsv.wu": ("hsv.wu xreg0, (xreg1)", ("xreg0", "xreg1"), (), (), ()),
    "wfi": ("wfi", (), (), (), ()),
}

trap_ret = {
    "mret": ("mret", (), (), (), ()),
    "sret": ("sret", (), (), (), ()),
    "uret": ("uret", (), (), (), ()),
}

cbo_instructions = {
    "cbo.clean": ("cbo.clean (xreg1)", ("xreg1",), (), (), ()),
    "cbo.flush": ("cbo.flush (xreg1)", ("xreg1",), (), (), ()),
    "cbo.inval": ("cbo.inval (xreg1)", ("xreg1",), (), (), ()),
    "prefetch.i": ("prefetch.i imm12(xreg1)", ("xreg1",), (), (("imm12", 32),), ()),
    "prefetch.r": ("prefetch.r imm12(xreg1)", ("xreg1",), (), (("imm12", 32),), ()),
    "prefetch.w": ("prefetch.w imm12(xreg1)", ("xreg1",), (), (("imm12", 32),), ()),
    "cbo.zero": ("cbo.zero (xreg1)", ("xreg1",), (), (), ()),
}

vector_configuration_setting_instructions = {
    "vsetvli": ("vsetvli xreg0, xreg1, {}", ("xreg0", "xreg1"), (), (), ()),
    "vsetvl": ("vsetvl xreg0, xreg1, xreg2", ("xreg0", "xreg1", "xreg2"), (), (), ()),
    # "vsetivli":
}

vector_load_store_instructions = {
    "vle8.v": ("vle8.v {}, (xreg1)", ("xreg1",), (), (), ()),
    "vle16.v": ("vle16.v {}, (xreg1)", ("xreg1",), (), (), ()),
    "vle32.v": ("vle32.v {}, (xreg1)", ("xreg1",), (), (), ()),
    "vle64.v": ("vle64.v {}, (xreg1)", ("xreg1",), (), (), ()),
    "vse8.v": ("vse8.v {}, (xreg1)", ("xreg1",), (), (), ()),
    "vse16.v": ("vse16.v {}, (xreg1)", ("xreg1",), (), (), ()),
    "vse32.v": ("vse32.v {}, (xreg1)", ("xreg1",), (), (), ()),
    "vse64.v": ("vse64.v {}, (xreg1)", ("xreg1",), (), (), ()),
    "vlm.v": ("vlm.v {}, (xreg1)", ("xreg1",), (), (), ()),
    "vsm.v": ("vsw.v {}, (xreg1)", ("xreg1",), (), (), ()),
    "vlse8.v": ("vlse8.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vlse16.v": ("vlse16.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vlse32.v": ("vlse32.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vlse64.v": ("vlse64.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vsse8.v": ("vsse8.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vsse16.v": ("vsse16.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vsse32.v": ("vsse32.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vsse64.v": ("vsse64.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vluxei8.v": ("vluxei8.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vluxei16.v": ("vluxei16.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vluxei32.v": ("vluxei32.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vluxei64.v": ("vluxei64.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vloxei8.v": ("vloxei8.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vloxei16.v": ("vloxei16.v {},(xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vloxei32.v": ("vloxei32.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vloxei64.v": ("vloxei64.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vsuxei8.v": ("vsuxei8.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vsuxei16.v": ("vsuxei16.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vsuxei32.v": ("vsuxei32.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vsuxei64.v": ("vsuxei64.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vsoxei8.v": ("vsoxei8.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vsoxei16.v": ("vsoxei16.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vsoxei32.v": ("vsoxei32.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
    "vsoxei64.v": ("vsoxei64.v {}, (xreg1), xreg2", ("xreg1", "xreg2"), (), (), ()),
}


vector_indexed_instructions = {
    # "vlxb.v": ("vlxb.v {}, (xreg1), {}", ("xreg1",), (), (), ()),
    # "vlxh.v": ("vlxh.v {}, (xreg1), {}", ("xreg1",), (), (), ()),
    # "vlxw.v": ("vlxw.v {}, (xreg1), {}", ("xreg1",), (), (), ()),
    # "vlxbu.v": ("vlxbu.v {}, (xreg1), {}", ("xreg1",), (), (), ()),
    # "vlxhu.v": ("vlxhu.v {}, (xreg1), {}", ("xreg1",), (), (), ()),
    # "vlxwu.v": ("vlxwu.v {}, (xreg1), {}", ("xreg1",), (), (), ()),
    # "vlxe.v": ("vlxe.v {}, (xreg1), {}", ("xreg1",), (), (), ()),
    # "vsxb.v": ("vsxb.v {}, (xreg1), {}", ("xreg1",), (), (), ()),
    # "vsxh.v": ("vsxh.v {}, (xreg1), {}", ("xreg1",), (), (), ()),
    # "vsxw.v": ("vsxw.v {}, (xreg1), {}", ("xreg1",), (), (), ()),
    # "vsxe.v": ("vsxe.v {}, (xreg1), {}", ("xreg1",), (), (), ()),
    # "vsuxb.v": ("vsuxb.v {}, (xreg1), {}", ("xreg1",), (), (), ()),
    # "vsuxh.v": ("vsuxh.v {}, (xreg1), {}", ("xreg1",), (), (), ()),
    # "vsuxw.v": ("vsuxw.v {}, (xreg1), {}", ("xreg1",), (), (), ()),
    # "vsuxe.v": ("vsuxe.v {}, (xreg1), {}", ("xreg1",), (), (), ()),
}

vector_segment_loads_and_stores = {
    # "vlseg": ("vlseg{}{}.v {}, (xreg1)", ("xreg1",), (), (), ()),
    # "vsseg": ("vlseg{}{}.v {}, (xreg1)", ("xreg1",), (), (), ()),
}

rv_vector = {}
rv_vector.update(vector_configuration_setting_instructions)
rv_vector.update(vector_load_store_instructions)
rv_vector.update(vector_indexed_instructions)
rv_vector.update(vector_segment_loads_and_stores)

rv32i = {}
rv32i.update(rv32i_rtype)
rv32i.update(rv32i_itype)
rv32i.update(rv32i_btype)
rv32i.update(rv32i_stype)
rv32i.update(rv32i_jtype)
rv32i.update(rv32i_utype)

rv64i = {}
rv64i.update(rv64i_itype)
rv64i.update(rv64i_stype)

rv32m = rv32m_rtype
rv64m = rv64m_rtype

rv32a = rv32a_rtype
rv64a = rv64a_rtype

rv32f = {}
rv32f.update(rv32f_rtype)
rv32f.update(rv32f_r4type)
rv32f.update(rv32f_itype)
rv32f.update(rv32f_stype)

rv64f = rv64f_rtype

rv32d = {}
rv32d.update(rv32d_rtype)
rv32d.update(rv32d_r4type)
rv32d.update(rv32d_itype)
rv32d.update(rv32d_stype)

rv64d = rv64d_rtype

rv32q = {}
rv32q.update(rv32q_rtype)
rv32q.update(rv32q_r4type)
rv32q.update(rv32q_itype)
rv32q.update(rv32q_stype)

rv64q = rv64q_rtype

rv64 = {}
rv64.update(rv64i)
rv64.update(rv64m)
rv64.update(rv64a)
rv64.update(rv64f)
rv64.update(rv64d)
rv64.update(rv64q)

rv_opcodes = {
    "rv32i": rv32i,
    "rv64i": rv64i,
    "rv_zifencei": rv_zifencei,
    "rv_zicsr": rv_zicsr,
    "rv32m": rv32m,
    "rv64m": rv64m,
    "rv32a": rv32a,
    "rv64a": rv64a,
    "rv32f": rv32f,
    "rv64f": rv64f,
    "rv32d": rv32d,
    "rv64d": rv64d,
    "rv32q": rv32q,
    "rv64q": rv64q,
    "trap_ret": trap_ret,
}

""" RISCV Register Names """

xreg_names = (
    "zero",
    "ra",
    "sp",
    "gp",
    "tp",
    "t0",
    "t1",
    "t2",
    "s0",
    "s1",
    "a0",
    "a1",
    "a2",
    "a3",
    "a4",
    "a5",
    "a6",
    "a7",
    "s2",
    "s3",
    "s4",
    "s5",
    "s6",
    "s7",
    "s8",
    "s9",
    "s10",
    "s11",
    "t3",
    "t4",
    "t5",
    "t6",
)
freg_names = (
    "ft0",
    "ft1",
    "ft2",
    "ft3",
    "ft4",
    "ft5",
    "ft6",
    "ft7",
    "fs0",
    "fs1",
    "fa0",
    "fa1",
    "fa2",
    "fa3",
    "fa4",
    "fa5",
    "fa6",
    "fa7",
    "fs2",
    "fs3",
    "fs4",
    "fs5",
    "fs6",
    "fs7",
    "fs8",
    "fs9",
    "fs10",
    "fs11",
    "ft8",
    "ft9",
    "ft10",
    "ft11",
)
csr_names = (
    "fflags",
    "frm",
    "fcsr",
    "sstatus",
    "sie",
    "sscratch",
    "sepc",
    "scause",
    "stval",
    "sip",
    "satp",
    "mhartid",
    "mstatus",
    "medeleg",
    "mie",
    "mscratch",
    "mepc",
    "mcause",
    "mtval",
    "mip",
    "pmpcfg0",
    "pmpaddr0",
    "pmpaddr1",
    "pmpaddr2",
    "pmpaddr3",
    "pmpaddr4",
    "pmpaddr5",
    "pmpaddr6",
    "pmpaddr7",
)

# m-mode
# 0xBC2 mbmc
csr_bitmap = ("0xBC2",)

# m-mode
# 0xBC3 mmpt
csr_mpt = ("0xBC3",)

csrs_cbo = ("menvcfg", "senvcfg", "henvcfg")

csrs_vector = ("vstart", "vxsat", "vxrm", "vl", "vtype")

vreg_names = (
    "v0",
    "v1",
    "v2",
    "v3",
    "v4",
    "v5",
    "v6",
    "v7",
    "v8",
    "v9",
    "v10",
    "v11",
    "v12",
    "v13",
    "v14",
    "v15",
    "v16",
    "v17",
    "v18",
    "v19",
    "v20",
    "v21",
    "v22",
    "v23",
    "v24",
    "v25",
    "v26",
    "v27",
    "v28",
    "v29",
    "v30",
    "v31",
)

counter_timers = (
    "cycle",
    "time",
    "instret",
    "cycleh",
    "timeh",
    "instreth",
    "hpmcounter3",
    "hpmcounter4",
    "hpmcounter5",
    "hpmcounter6",
    "hpmcounter7",
    "hpmcounter8",
    "hpmcounter31",
    "hpmcounter3h",
    "hpmcounter4h",
    "hpmcounter31h",
)

hv_csrs = (
    # Hypervisor Trap Setup
    "hstatus",
    "hedeleg",
    "hideleg",
    "hie",
    "hcounteren",
    "hgeie",
    "hedelegh",
    # Hypervisor Trap Handling
    "htval",
    "hip",
    "hvip",
    "htinst",
    "hgeip",
    # Hypervisor Configuration
    "henvcfg",
    "henvcfgh",
    # Hypervisor Protection and Translation
    "hgatp",
    # Debug/Trace Registers
    "hcontext",
    # Hypervisor Counter/Timer Virtualization Registers
    "htimedelta",
    "htimedeltah",
    # Hypervisor State Enable Registers
    "hstateen0",
    "hstateen1",
    "hstateen2",
    "hstateen3",
    "hstateen0h",
    "hstateen1h",
    "hstateen2h",
    "hstateen3h",
    # Virtual Supervisor Registers
    "vsstatus",
    "vsie",
    "vstvec",
    "vsscratch",
    "vsepc",
    "vscause",
    "vstval",
    "vsip",
    "vsatp",
)
# ['ustatus', 'uie', 'uepc', 'ucause', 'utval', 'uip']
# ['sedeleg', 'sideleg']
# ['pmpcfg1', 'pmpcfg2', 'pmpcfg3']
# [ 'utvec', 'stvec', 'mtvec', 'mcycle', 'minstret', 'mcycleh', 'minstreth' ]
# [ 'mcounteren', 'scounteren' ]
