#!/bin/bash
#
# @brief   gen_mmap
# @version 1.0.6
# @date    Sat Aug 08 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_mmap
pylint gen_mmap > gen_mmap.report
echo "Done"
