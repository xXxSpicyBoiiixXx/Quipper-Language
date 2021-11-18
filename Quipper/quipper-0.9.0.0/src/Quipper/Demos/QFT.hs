-- This file is part of Quipper. Copyright (C) 2011-2019. Please see the
-- file COPYRIGHT for a list of authors, copyright holders, licensing,
-- and other details. All rights reserved.
-- 
-- ======================================================================

import Quipper
import Quipper.Libraries.QFT

main :: IO ()
main = print_generic Preview qft_little_endian (replicate 5 qubit)
