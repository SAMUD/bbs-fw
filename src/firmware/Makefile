.PHONY: all clean

# Select target controller (normally done from cmd line):
# TARGET_CONTROLLER = BBSHD
# TARGET_CONTROLLER = BBS02

# Compiler
CC = sdcc

# Target name
TARGET = bbs-fw

MAINSRC = main.c

CFLAGS = -Ddouble=float --std-c99 -D$(TARGET_CONTROLLER)

# Target Specific
ifeq ($(TARGET_CONTROLLER), BBSHD)
	CFLAGS += -mmcs51 --model-large --xram-size 3840
endif

ifeq ($(TARGET_CONTROLLER), BBS02)
	CFLAGS += -mmcs51 --model-large --xram-size 1792
endif

INCS = $(wildcard *.h)
SRCS = $(filter-out main.c, $(wildcard *.c))
RELS := $(SRCS:.c=.rel)

INC_DIRS = -I./

all: precheck $(TARGET) hex

$(TARGET): $(MAINSRC) $(RELS)
	$(CC) -o $(TARGET).ihx $(INC_DIRS) $(CFLAGS) $(MAINSRC) $(RELS)

%.rel: %.c $(INCS)
	$(CC) -o $@ -c $(INC_DIRS) $(CFLAGS) $<

echo:
	$(info SRCS: $(SRCS))
	$(info RELS: $(RELS))
	$(info INCS: $(INCS))

precheck:
ifndef TARGET_CONTROLLER
	$(info TARGET_CONTROLLER is not specified.)
	$(info Set to one of [BBSHD, BBS02])
	$(info Example:)
	$(info $(null)  make all TARGET_CONTROLLER=BBSHD)
	$(error )
endif
	$(info Building bbs-fw for $(TARGET_CONTROLLER))

hex:
	@packihx bbs-fw.ihx > bbs-fw.hex

clean:
ifeq ($(UNAME), Linux)
	@rm -f *.hex
	@rm -f *.ihx
	@rm -f *.asm
	@rm -f *.rel
	@rm -f *.lk
	@rm -f *.lst
	@rm -f *.rst
	@rm -f *.sym
	@rm -f *.cdb
	@rm -f *.map
	@rm -f *.elf
	@rm -f *.adb
	@rm -f *.mem
else
	@cmd /C clean.bat
endif
	$(info Clean Finished)

.PHONY = all hex clean precheck echo
.SUFFIXES: .c .rel
