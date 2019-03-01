{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf200
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red191\green100\blue38;\red32\green32\blue32;\red153\green168\blue186;
\red88\green118\blue71;\red254\green187\blue91;\red117\green114\blue185;\red173\green169\blue32;\red86\green132\blue173;
\red152\green54\blue29;\red109\green109\blue109;}
{\*\expandedcolortbl;;\csgenericrgb\c74902\c39216\c14902;\csgenericrgb\c12549\c12549\c12549;\csgenericrgb\c60000\c65882\c72941;
\csgenericrgb\c34510\c46275\c27843;\csgenericrgb\c99608\c73333\c35686;\csgenericrgb\c45882\c44706\c72549;\csgenericrgb\c67843\c66275\c12549;\csgenericrgb\c33725\c51765\c67843;
\csgenericrgb\c59608\c21176\c11373;\csgenericrgb\c42745\c42745\c42745;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs24 \cf2 \cb3 import \cf4 random\
\cf2 import \cf4 time\
\cf2 import \cf4 pytest\
\cf5 """\
download plugins from http://plugincompat.herokuapp.com/\
"""\
\cf2 import \cf4 time\
\cf2 def \cf6 timing\cf4 (func):\
    \cf2 def \cf6 wrapper\cf4 ():\
        start = time.time()\
        func()\
        finish = time.time()\
        \cf7 print\cf4 (\cf5 'Elapsed time: \{\}'\cf4 .format(finish - start))\
    \cf2 return \cf4 wrapper\
\
\cf8 @timing\
@pytest.mark.parametrize\cf4 (\cf5 "test_input, expected_output"\cf2 , \cf4 [(\cf9 5\cf2 , \cf9 10\cf4 )\cf2 , \cf4 (\cf9 2\cf2 , \cf9 4\cf4 )])\
\cf2 def \cf6 test_method1\cf4 (test_input\cf2 , \cf4 expected_output):\
    total = test_input * \cf9 2\
    \cf2 assert \cf4 total == expected_output\
\
\
\
\cf8 @timing\
@pytest.fixture\cf4 (\cf10 scope\cf4 =\cf5 "module"\cf4 )\
\cf2 def \cf6 setUp\cf4 ():\
    \cf7 print\cf4 (\cf5 "setup method is running now!"\cf4 )\
    \cf2 yield\
    \cf7 print\cf4 (\cf5 "teardown at the end of last test"\cf4 )\
\
\cf2 def \cf6 test_calc_multiply\cf4 (setUp):\
    result = \cf9 10 \cf4 * \cf9 3\
    \cf2 assert \cf4 result == \cf9 30\
\
\cf8 @pytest.mark.skip\cf4 (\cf5 "dont want to execute on the current build"\cf4 )\
\cf2 def \cf6 test_another_calc_Test\cf4 ():\
    \cf2 pass\
\
\cf4 a = \cf9 101\
\cf8 @pytest.mark.skipif\cf4 (a>\cf9 100\cf2 , \cf10 reason\cf4 =\cf5 "blah"\cf4 )\
\cf2 def \cf6 test_failure\cf4 ():\
    \cf2 assert \cf9 1\cf4 ==\cf9 1\
\
\cf8 @pytest.mark.Smoke\
\cf2 def \cf6 test_sm1\cf4 ():\
    \cf2 pass\
\
\cf8 @pytest.mark.full\
\cf2 def \cf6 test_sanity1\cf4 (setUp):\
    \cf2 pass\
\
\cf8 @pytest.mark.Sanity\
\cf2 def \cf6 test_sanity2\cf4 ():\
    \cf2 pass\
\
\cf8 @pytest.mark.full\
\cf2 def \cf6 test_Asserts\cf4 ():\
    a\cf2 ,\cf4 b=\cf9 1\cf2 ,\cf9 2\
    \cf2 assert\cf4 (a==b\cf2 , \cf5 "This should fail."\cf4 )\
    \cf11 # if a != b:\
    #     raise ArithmeticError("they ara not equal!")\
\
\cf8 @pytest.mark.xfail\
\cf2 def \cf6 test_list_assertion\cf4 ():\
    a = [\cf9 1\cf2 ,\cf9 2\cf2 ,\cf9 3\cf2 ,\cf9 4\cf4 ]\
    b = [\cf9 1\cf2 ,\cf9 2\cf2 ,\cf9 4\cf2 ,\cf9 3\cf4 ]\
    \cf2 assert \cf4 a == b\
\
\cf8 @pytest.mark.smoke\
\cf2 def \cf6 test_marks\cf4 ():\
    \cf2 assert \cf9 1 \cf4 == \cf9 1\
\
\cf8 @pytest.mark.xfail\cf4 (\cf10 reason\cf4 =\cf5 "flaky test , jira #123"\cf2 , \cf10 strict\cf4 =\cf2 False\cf4 )\
\cf2 def \cf6 test_flakyTest\cf4 ():\
    \cf2 assert \cf4 random.randint(\cf9 1\cf2 ,\cf9 3\cf4 ) == \cf9 2\
\
\
\
}