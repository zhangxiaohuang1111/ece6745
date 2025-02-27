#=========================================================================
# Proc_rimm_test.py
#=========================================================================
# It is as simple as inheriting from FL tests and change the ProcType.

from proc.Proc import Proc
from proc.test.ProcFL_rimm_test import Tests as ProcFL_rimm_TestsBaseClass

#-------------------------------------------------------------------------
# Tests
#-------------------------------------------------------------------------

class Tests( ProcFL_rimm_TestsBaseClass ):

  @classmethod
  def setup_class( cls ):
    cls.ProcType = Proc

