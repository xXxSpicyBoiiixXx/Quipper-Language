# This file is part of Quipper. Copyright (C) 2011-2019. Please see the
# file COPYRIGHT for a list of authors, copyright holders, licensing,
# and other details. All rights reserved.
# 
# ======================================================================


MODULES = Quipper.hs Quipper/Internal/CircLifting.hs		\
 Quipper/Internal/Circuit.hs Quipper/Internal/Classical.hs	\
 Quipper/Internal/Control.hs Quipper/Internal/Generic.hs	\
 Quipper/Internal.hs Quipper/Internal/Labels.hs			\
 Quipper/Internal/Monad.hs Quipper/Internal/Printing.hs		\
 Quipper/Internal/QClasses.hs Quipper/Internal/QData.hs		\
 Quipper/Internal/Transformer.hs
TARGET = Quipper.hi
SUBPACKAGE = quipper
SUBDIR = src
SUBDIR_ROOT = src
SUBDIR_REL = .
BASEDIR = ..
CLEAN_SUBDIRS = Quipper Quipper/Internal Quipper/Internal/Template

SCRIPTS=convert_template.awk convert_template.bat	\
 convert_template.sh quipper quipperi quipperdoc quipperdoc.bat	\
 quipper.bat quipperi.bat
EXTRA_DIST=$(SCRIPTS:%=../scripts/%)

include $(BASEDIR)/Makefile.common
