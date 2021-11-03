# This file is part of Quipper. Copyright (C) 2011-2019. Please see the
# file COPYRIGHT for a list of authors, copyright holders, licensing,
# and other details. All rights reserved.
# 
# ======================================================================


MODULES = Auxiliary.hs CommandLine.hs Preview.hs PortableSignals.hs	\
          RandomSource.hs Sampling.hs Stabilizers/Pauli.hs		\
          Stabilizers/Clifford.hs Template.hs Template/Auxiliary.hs	\
          Template/ErrorMsgQ.hs Template/Lifting.hs Template/LiftQ.hs	\
          Tuple.hs Typeable.hs
TARGET = $(MODULES:%.hs=%.hi)
SUBPACKAGE = auxiliary
SUBDIR = src/Quipper/Utils
SUBDIR_ROOT = src
SUBDIR_REL = Quipper/Utils
BASEDIR = ../../..
CLEAN_SUBDIRS = Stabilizers QuipperASCIIParser Template

include $(BASEDIR)/Makefile.common
