Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\DANISH LAPTOP\Downloads\FASDH25-portfolio2\scripts\regex_script_mubashir_alizain_iqra.py.py
gaza:
2023-10:4168
2023-11:4527
2023-12:2863
2024-01:1956
2024-02:1882
2024-03:2197
2024-04:993
gaza strip:
2023-10:4168
2023-11:4527
2023-12:2863
2024-01:1956
2024-02:1882
2024-03:2197
2024-04:993
gaza city:
2023-10:4174
2023-11:4529
2023-12:2865
2024-01:1956
2024-02:1882
2024-03:2199
2024-04:993
rafah:
2023-10:182
2023-11:150
2023-12:201
2024-01:41
2024-02:497
2024-03:253
2024-04:81
bayt lahya:
2023-10:11
2023-11:14
2023-12:8
2024-01:2
2024-02:3
2024-03:1
2024-04:2
jabalya:
2023-10:37
2023-11:103
2023-12:46
2024-01:12
2024-02:7
2024-03:8
2024-04:3
jabalia:
2023-10:33
2023-11:102
2023-12:44
2024-01:12
2024-02:7
2024-03:8
2024-04:2
bayt hanun:
2023-10:19
2023-11:17
2023-12:4
2024-01:1
2024-02:3
2024-03:7
2024-04:10
al-shifa hospital:
2023-10:31
2023-11:242
2023-12:23
2024-01:3
2024-02:15
2024-03:32
2024-04:13
khan younis:
2023-10:74
2023-11:132
2023-12:173
2024-01:74
2024-02:63
2024-03:40
2024-04:25
tunis:
2023-10:3
2023-11:4
2023-12:1
al burayj:
2023-10:3
2023-11:15
2023-12:17
2024-01:5
2024-02:2
2024-03:5
bureij:
2023-10:3
2023-11:15
2023-12:17
2024-01:5
2024-02:2
2024-03:5
remal:
2023-10:14
2023-11:3
2023-12:5
2024-03:3
2024-04:2
deir el-balah:
2023-10:38
2023-11:51
2023-12:45
2024-01:19
2024-02:31
2024-03:30
2024-04:12
an nusayrat:
2023-10:22
2023-11:16
2023-12:26
2024-01:11
2024-02:6
2024-03:9
2024-04:8
nuseirat:
2023-10:22
2023-11:16
2023-12:26
2024-01:11
2024-02:6
2024-03:9
2024-04:8
maghazi:
2023-10:15
2023-11:28
2023-12:49
2024-01:9
2024-02:2
2024-03:3
abu sittah:
2023-10:1
2023-12:4
2024-04:4
hijazi:
2023-10:2
2023-11:2
2023-12:1
2024-01:1
2024-04:2
bani suhayla:
2023-10:1
2023-11:1
2023-12:1
2024-01:2
abasan al kabirah:
2023-10:4
2023-11:5
2023-12:4
2024-02:1
az-zawayda:
2023-10:1
2023-12:1
2024-02:1
2024-04:1
shokat as-sufi:
2023-10:1
al-mughraqa:
2023-10:1
2024-01:1
abasan al-saghira:
2023-10:1
2023-11:2
qizan:
2023-10:1
al-azhar university:
2023-10:2
2023-11:1
2023-12:2
2024-01:1
al-aqsa university:
2023-10:1
2024-01:2
2024-02:2
bani suhela:
2023-10:3
2023-11:5
2024-03:2
al qararah:
2023-11:1
2024-01:1
2024-03:1
an nasr:
2024-01:1
al mawasi:
2024-01:1
2024-03:1
al amal:
2024-01:1
2024-03:1
al mu'askar:
2024-01:1
markaz al madinah:
2024-01:1
hamadah:
2024-02:1
Traceback (most recent call last):
  File "C:\Users\DANISH LAPTOP\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 939, in _finalize_columns_and_data
    columns = _validate_or_indexify_columns(contents, columns)
  File "C:\Users\DANISH LAPTOP\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 986, in _validate_or_indexify_columns
    raise AssertionError(
AssertionError: 2 columns passed, passed data had 3 columns

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\DANISH LAPTOP\Downloads\FASDH25-portfolio2\scripts\regex_script_mubashir_alizain_iqra.py.py", line 89, in <module>
    df = pd.DataFrame(rows, columns = columns)
  File "C:\Users\DANISH LAPTOP\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 851, in __init__
    arrays, columns, index = nested_data_to_arrays(
  File "C:\Users\DANISH LAPTOP\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 520, in nested_data_to_arrays
    arrays, columns = to_arrays(data, columns, dtype=dtype)
  File "C:\Users\DANISH LAPTOP\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 845, in to_arrays
    content, columns = _finalize_columns_and_data(arr, columns, dtype)
  File "C:\Users\DANISH LAPTOP\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 942, in _finalize_columns_and_data
    raise ValueError(err) from err
ValueError: 2 columns passed, passed data had 3 columns

= RESTART: C:\Users\DANISH LAPTOP\Downloads\FASDH25-portfolio2\scripts\regex_script_mubashir_alizain_iqra.py.py
gaza:
2023-10:4168
2023-11:4527
2023-12:2863
2024-01:1956
2024-02:1882
2024-03:2197
2024-04:993
gaza strip:
2023-10:4168
2023-11:4527
2023-12:2863
2024-01:1956
2024-02:1882
2024-03:2197
2024-04:993
gaza city:
2023-10:4174
2023-11:4529
2023-12:2865
2024-01:1956
2024-02:1882
2024-03:2199
2024-04:993
rafah:
2023-10:182
2023-11:150
2023-12:201
2024-01:41
2024-02:497
2024-03:253
2024-04:81
bayt lahya:
2023-10:11
2023-11:14
2023-12:8
2024-01:2
2024-02:3
2024-03:1
2024-04:2
jabalya:
2023-10:37
2023-11:103
2023-12:46
2024-01:12
2024-02:7
2024-03:8
2024-04:3
jabalia:
2023-10:33
2023-11:102
2023-12:44
2024-01:12
2024-02:7
2024-03:8
2024-04:2
bayt hanun:
2023-10:19
2023-11:17
2023-12:4
2024-01:1
2024-02:3
2024-03:7
2024-04:10
al-shifa hospital:
2023-10:31
2023-11:242
2023-12:23
2024-01:3
2024-02:15
2024-03:32
2024-04:13
khan younis:
2023-10:74
2023-11:132
2023-12:173
2024-01:74
2024-02:63
2024-03:40
2024-04:25
tunis:
2023-10:3
2023-11:4
2023-12:1
al burayj:
2023-10:3
2023-11:15
2023-12:17
2024-01:5
2024-02:2
2024-03:5
bureij:
2023-10:3
2023-11:15
2023-12:17
2024-01:5
2024-02:2
2024-03:5
remal:
2023-10:14
2023-11:3
2023-12:5
2024-03:3
2024-04:2
deir el-balah:
2023-10:38
2023-11:51
2023-12:45
2024-01:19
2024-02:31
2024-03:30
2024-04:12
an nusayrat:
2023-10:22
2023-11:16
2023-12:26
2024-01:11
2024-02:6
2024-03:9
2024-04:8
nuseirat:
2023-10:22
2023-11:16
2023-12:26
2024-01:11
2024-02:6
2024-03:9
2024-04:8
maghazi:
2023-10:15
2023-11:28
2023-12:49
2024-01:9
2024-02:2
2024-03:3
abu sittah:
2023-10:1
2023-12:4
2024-04:4
hijazi:
2023-10:2
2023-11:2
2023-12:1
2024-01:1
2024-04:2
bani suhayla:
2023-10:1
2023-11:1
2023-12:1
2024-01:2
abasan al kabirah:
2023-10:4
2023-11:5
2023-12:4
2024-02:1
az-zawayda:
2023-10:1
2023-12:1
2024-02:1
2024-04:1
shokat as-sufi:
2023-10:1
al-mughraqa:
2023-10:1
2024-01:1
abasan al-saghira:
2023-10:1
2023-11:2
qizan:
2023-10:1
al-azhar university:
2023-10:2
2023-11:1
2023-12:2
2024-01:1
al-aqsa university:
2023-10:1
2024-01:2
2024-02:2
bani suhela:
2023-10:3
2023-11:5
2024-03:2
al qararah:
2023-11:1
2024-01:1
2024-03:1
an nasr:
2024-01:1
al mawasi:
2024-01:1
2024-03:1
al amal:
2024-01:1
2024-03:1
al mu'askar:
2024-01:1
markaz al madinah:
2024-01:1
hamadah:
2024-02:1
Traceback (most recent call last):
  File "C:\Users\DANISH LAPTOP\Downloads\FASDH25-portfolio2\scripts\regex_script_mubashir_alizain_iqra.py.py", line 85, in <module>
    for main_name, months in mentions_per_month:
ValueError: too many values to unpack (expected 2)

= RESTART: C:\Users\DANISH LAPTOP\Downloads\FASDH25-portfolio2\scripts\regex_script_mubashir_alizain_iqra.py.py
gaza:
2023-10:4168
2023-11:4527
2023-12:2863
2024-01:1956
2024-02:1882
2024-03:2197
2024-04:993
gaza strip:
2023-10:4168
2023-11:4527
2023-12:2863
2024-01:1956
2024-02:1882
2024-03:2197
2024-04:993
gaza city:
2023-10:4174
2023-11:4529
2023-12:2865
2024-01:1956
2024-02:1882
2024-03:2199
2024-04:993
rafah:
2023-10:182
2023-11:150
2023-12:201
2024-01:41
2024-02:497
2024-03:253
2024-04:81
bayt lahya:
2023-10:11
2023-11:14
2023-12:8
2024-01:2
2024-02:3
2024-03:1
2024-04:2
jabalya:
2023-10:37
2023-11:103
2023-12:46
2024-01:12
2024-02:7
2024-03:8
2024-04:3
jabalia:
2023-10:33
2023-11:102
2023-12:44
2024-01:12
2024-02:7
2024-03:8
2024-04:2
bayt hanun:
2023-10:19
2023-11:17
2023-12:4
2024-01:1
2024-02:3
2024-03:7
2024-04:10
al-shifa hospital:
2023-10:31
2023-11:242
2023-12:23
2024-01:3
2024-02:15
2024-03:32
2024-04:13
khan younis:
2023-10:74
2023-11:132
2023-12:173
2024-01:74
2024-02:63
2024-03:40
2024-04:25
tunis:
2023-10:3
2023-11:4
2023-12:1
al burayj:
2023-10:3
2023-11:15
2023-12:17
2024-01:5
2024-02:2
2024-03:5
bureij:
2023-10:3
2023-11:15
2023-12:17
2024-01:5
2024-02:2
2024-03:5
remal:
2023-10:14
2023-11:3
2023-12:5
2024-03:3
2024-04:2
deir el-balah:
2023-10:38
2023-11:51
2023-12:45
2024-01:19
2024-02:31
2024-03:30
2024-04:12
an nusayrat:
2023-10:22
2023-11:16
2023-12:26
2024-01:11
2024-02:6
2024-03:9
2024-04:8
nuseirat:
2023-10:22
2023-11:16
2023-12:26
2024-01:11
2024-02:6
2024-03:9
2024-04:8
maghazi:
2023-10:15
2023-11:28
2023-12:49
2024-01:9
2024-02:2
2024-03:3
abu sittah:
2023-10:1
2023-12:4
2024-04:4
hijazi:
2023-10:2
2023-11:2
2023-12:1
2024-01:1
2024-04:2
bani suhayla:
2023-10:1
2023-11:1
2023-12:1
2024-01:2
abasan al kabirah:
2023-10:4
2023-11:5
2023-12:4
2024-02:1
az-zawayda:
2023-10:1
2023-12:1
2024-02:1
2024-04:1
shokat as-sufi:
2023-10:1
al-mughraqa:
2023-10:1
2024-01:1
abasan al-saghira:
2023-10:1
2023-11:2
qizan:
2023-10:1
al-azhar university:
2023-10:2
2023-11:1
2023-12:2
2024-01:1
al-aqsa university:
2023-10:1
2024-01:2
2024-02:2
bani suhela:
2023-10:3
2023-11:5
2024-03:2
al qararah:
2023-11:1
2024-01:1
2024-03:1
an nasr:
2024-01:1
al mawasi:
2024-01:1
2024-03:1
al amal:
2024-01:1
2024-03:1
al mu'askar:
2024-01:1
markaz al madinah:
2024-01:1
hamadah:
2024-02:1
Traceback (most recent call last):
  File "C:\Users\DANISH LAPTOP\Downloads\FASDH25-portfolio2\scripts\regex_script_mubashir_alizain_iqra.py.py", line 85, in <module>
    for main_name, months in mentions_per_month:
ValueError: too many values to unpack (expected 2)

= RESTART: C:\Users\DANISH LAPTOP\Downloads\FASDH25-portfolio2\scripts\regex_script_mubashir_alizain_iqra.py.py
gaza:
2023-10:4168
2023-11:4527
2023-12:2863
2024-01:1956
2024-02:1882
2024-03:2197
2024-04:993
gaza strip:
2023-10:4168
2023-11:4527
2023-12:2863
2024-01:1956
2024-02:1882
2024-03:2197
2024-04:993
gaza city:
2023-10:4174
2023-11:4529
2023-12:2865
2024-01:1956
2024-02:1882
2024-03:2199
2024-04:993
rafah:
2023-10:182
2023-11:150
2023-12:201
2024-01:41
2024-02:497
2024-03:253
2024-04:81
bayt lahya:
2023-10:11
2023-11:14
2023-12:8
2024-01:2
2024-02:3
2024-03:1
2024-04:2
jabalya:
2023-10:37
2023-11:103
2023-12:46
2024-01:12
2024-02:7
2024-03:8
2024-04:3
jabalia:
2023-10:33
2023-11:102
2023-12:44
2024-01:12
2024-02:7
2024-03:8
2024-04:2
bayt hanun:
2023-10:19
2023-11:17
2023-12:4
2024-01:1
2024-02:3
2024-03:7
2024-04:10
al-shifa hospital:
2023-10:31
2023-11:242
2023-12:23
2024-01:3
2024-02:15
2024-03:32
2024-04:13
khan younis:
2023-10:74
2023-11:132
2023-12:173
2024-01:74
2024-02:63
2024-03:40
2024-04:25
tunis:
2023-10:3
2023-11:4
2023-12:1
al burayj:
2023-10:3
2023-11:15
2023-12:17
2024-01:5
2024-02:2
2024-03:5
bureij:
2023-10:3
2023-11:15
2023-12:17
2024-01:5
2024-02:2
2024-03:5
remal:
2023-10:14
2023-11:3
2023-12:5
2024-03:3
2024-04:2
deir el-balah:
2023-10:38
2023-11:51
2023-12:45
2024-01:19
2024-02:31
2024-03:30
2024-04:12
an nusayrat:
2023-10:22
2023-11:16
2023-12:26
2024-01:11
2024-02:6
2024-03:9
2024-04:8
nuseirat:
2023-10:22
2023-11:16
2023-12:26
2024-01:11
2024-02:6
2024-03:9
2024-04:8
maghazi:
2023-10:15
2023-11:28
2023-12:49
2024-01:9
2024-02:2
2024-03:3
abu sittah:
2023-10:1
2023-12:4
2024-04:4
hijazi:
2023-10:2
2023-11:2
2023-12:1
2024-01:1
2024-04:2
bani suhayla:
2023-10:1
2023-11:1
2023-12:1
2024-01:2
abasan al kabirah:
2023-10:4
2023-11:5
2023-12:4
2024-02:1
az-zawayda:
2023-10:1
2023-12:1
2024-02:1
2024-04:1
shokat as-sufi:
2023-10:1
al-mughraqa:
2023-10:1
2024-01:1
abasan al-saghira:
2023-10:1
2023-11:2
qizan:
2023-10:1
al-azhar university:
2023-10:2
2023-11:1
2023-12:2
2024-01:1
al-aqsa university:
2023-10:1
2024-01:2
2024-02:2
bani suhela:
2023-10:3
2023-11:5
2024-03:2
al qararah:
2023-11:1
2024-01:1
2024-03:1
an nasr:
2024-01:1
al mawasi:
2024-01:1
2024-03:1
al amal:
2024-01:1
2024-03:1
al mu'askar:
2024-01:1
markaz al madinah:
2024-01:1
hamadah:
2024-02:1
Traceback (most recent call last):
  File "C:\Users\DANISH LAPTOP\Downloads\FASDH25-portfolio2\scripts\regex_script_mubashir_alizain_iqra.py.py", line 85, in <module>
    for main_name, months in mentions_per_month:
ValueError: too many values to unpack (expected 2)

= RESTART: C:\Users\DANISH LAPTOP\Downloads\FASDH25-portfolio2\scripts\regex_script_mubashir_alizain_iqra.py.py
gaza:
2023-10:4168
2023-11:4527
2023-12:2863
2024-01:1956
2024-02:1882
2024-03:2197
2024-04:993
gaza strip:
2023-10:4168
2023-11:4527
2023-12:2863
2024-01:1956
2024-02:1882
2024-03:2197
2024-04:993
gaza city:
2023-10:4174
2023-11:4529
2023-12:2865
2024-01:1956
2024-02:1882
2024-03:2199
2024-04:993
rafah:
2023-10:182
2023-11:150
2023-12:201
2024-01:41
2024-02:497
2024-03:253
2024-04:81
bayt lahya:
2023-10:11
2023-11:14
2023-12:8
2024-01:2
2024-02:3
2024-03:1
2024-04:2
jabalya:
2023-10:37
2023-11:103
2023-12:46
2024-01:12
2024-02:7
2024-03:8
2024-04:3
jabalia:
2023-10:33
2023-11:102
2023-12:44
2024-01:12
2024-02:7
2024-03:8
2024-04:2
bayt hanun:
2023-10:19
2023-11:17
2023-12:4
2024-01:1
2024-02:3
2024-03:7
2024-04:10
al-shifa hospital:
2023-10:31
2023-11:242
2023-12:23
2024-01:3
2024-02:15
2024-03:32
2024-04:13
khan younis:
2023-10:74
2023-11:132
2023-12:173
2024-01:74
2024-02:63
2024-03:40
2024-04:25
tunis:
2023-10:3
2023-11:4
2023-12:1
al burayj:
2023-10:3
2023-11:15
2023-12:17
2024-01:5
2024-02:2
2024-03:5
bureij:
2023-10:3
2023-11:15
2023-12:17
2024-01:5
2024-02:2
2024-03:5
remal:
2023-10:14
2023-11:3
2023-12:5
2024-03:3
2024-04:2
deir el-balah:
2023-10:38
2023-11:51
2023-12:45
2024-01:19
2024-02:31
2024-03:30
2024-04:12
an nusayrat:
2023-10:22
2023-11:16
2023-12:26
2024-01:11
2024-02:6
2024-03:9
2024-04:8
nuseirat:
2023-10:22
2023-11:16
2023-12:26
2024-01:11
2024-02:6
2024-03:9
2024-04:8
maghazi:
2023-10:15
2023-11:28
2023-12:49
2024-01:9
2024-02:2
2024-03:3
abu sittah:
2023-10:1
2023-12:4
2024-04:4
hijazi:
2023-10:2
2023-11:2
2023-12:1
2024-01:1
2024-04:2
bani suhayla:
2023-10:1
2023-11:1
2023-12:1
2024-01:2
abasan al kabirah:
2023-10:4
2023-11:5
2023-12:4
2024-02:1
az-zawayda:
2023-10:1
2023-12:1
2024-02:1
2024-04:1
shokat as-sufi:
2023-10:1
al-mughraqa:
2023-10:1
2024-01:1
abasan al-saghira:
2023-10:1
2023-11:2
qizan:
2023-10:1
al-azhar university:
2023-10:2
2023-11:1
2023-12:2
2024-01:1
al-aqsa university:
2023-10:1
2024-01:2
2024-02:2
bani suhela:
2023-10:3
2023-11:5
2024-03:2
al qararah:
2023-11:1
2024-01:1
2024-03:1
an nasr:
2024-01:1
al mawasi:
2024-01:1
2024-03:1
al amal:
2024-01:1
2024-03:1
al mu'askar:
2024-01:1
markaz al madinah:
2024-01:1
hamadah:
2024-02:1
Traceback (most recent call last):
  File "C:\Users\DANISH LAPTOP\Downloads\FASDH25-portfolio2\scripts\regex_script_mubashir_alizain_iqra.py.py", line 86, in <module>
    for month, n_matches in months.items:
TypeError: 'builtin_function_or_method' object is not iterable

= RESTART: C:\Users\DANISH LAPTOP\Downloads\FASDH25-portfolio2\scripts\regex_script_mubashir_alizain_iqra.py.py
gaza:
2023-10:4168
2023-11:4527
2023-12:2863
2024-01:1956
2024-02:1882
2024-03:2197
2024-04:993
gaza strip:
2023-10:4168
2023-11:4527
2023-12:2863
2024-01:1956
2024-02:1882
2024-03:2197
2024-04:993
gaza city:
2023-10:4174
2023-11:4529
2023-12:2865
2024-01:1956
2024-02:1882
2024-03:2199
2024-04:993
rafah:
2023-10:182
2023-11:150
2023-12:201
2024-01:41
2024-02:497
2024-03:253
2024-04:81
bayt lahya:
2023-10:11
2023-11:14
2023-12:8
2024-01:2
2024-02:3
2024-03:1
2024-04:2
jabalya:
2023-10:37
2023-11:103
2023-12:46
2024-01:12
2024-02:7
2024-03:8
2024-04:3
jabalia:
2023-10:33
2023-11:102
2023-12:44
2024-01:12
2024-02:7
2024-03:8
2024-04:2
bayt hanun:
2023-10:19
2023-11:17
2023-12:4
2024-01:1
2024-02:3
2024-03:7
2024-04:10
al-shifa hospital:
2023-10:31
2023-11:242
2023-12:23
2024-01:3
2024-02:15
2024-03:32
2024-04:13
khan younis:
2023-10:74
2023-11:132
2023-12:173
2024-01:74
2024-02:63
2024-03:40
2024-04:25
tunis:
2023-10:3
2023-11:4
2023-12:1
al burayj:
2023-10:3
2023-11:15
2023-12:17
2024-01:5
2024-02:2
2024-03:5
bureij:
2023-10:3
2023-11:15
2023-12:17
2024-01:5
2024-02:2
2024-03:5
remal:
2023-10:14
2023-11:3
2023-12:5
2024-03:3
2024-04:2
deir el-balah:
2023-10:38
2023-11:51
2023-12:45
2024-01:19
2024-02:31
2024-03:30
2024-04:12
an nusayrat:
2023-10:22
2023-11:16
2023-12:26
2024-01:11
2024-02:6
2024-03:9
2024-04:8
nuseirat:
2023-10:22
2023-11:16
2023-12:26
2024-01:11
2024-02:6
2024-03:9
2024-04:8
maghazi:
2023-10:15
2023-11:28
2023-12:49
2024-01:9
2024-02:2
2024-03:3
abu sittah:
2023-10:1
2023-12:4
2024-04:4
hijazi:
2023-10:2
2023-11:2
2023-12:1
2024-01:1
2024-04:2
bani suhayla:
2023-10:1
2023-11:1
2023-12:1
2024-01:2
abasan al kabirah:
2023-10:4
2023-11:5
2023-12:4
2024-02:1
az-zawayda:
2023-10:1
2023-12:1
2024-02:1
2024-04:1
shokat as-sufi:
2023-10:1
al-mughraqa:
2023-10:1
2024-01:1
abasan al-saghira:
2023-10:1
2023-11:2
qizan:
2023-10:1
al-azhar university:
2023-10:2
2023-11:1
2023-12:2
2024-01:1
al-aqsa university:
2023-10:1
2024-01:2
2024-02:2
bani suhela:
2023-10:3
2023-11:5
2024-03:2
al qararah:
2023-11:1
2024-01:1
2024-03:1
an nasr:
2024-01:1
al mawasi:
2024-01:1
2024-03:1
al amal:
2024-01:1
2024-03:1
al mu'askar:
2024-01:1
markaz al madinah:
2024-01:1
hamadah:
2024-02:1
Traceback (most recent call last):
  File "C:\Users\DANISH LAPTOP\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 939, in _finalize_columns_and_data
    columns = _validate_or_indexify_columns(contents, columns)
  File "C:\Users\DANISH LAPTOP\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 986, in _validate_or_indexify_columns
    raise AssertionError(
AssertionError: 2 columns passed, passed data had 3 columns

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\DANISH LAPTOP\Downloads\FASDH25-portfolio2\scripts\regex_script_mubashir_alizain_iqra.py.py", line 89, in <module>
    df = pd.DataFrame(rows, columns = columns)
  File "C:\Users\DANISH LAPTOP\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 851, in __init__
    arrays, columns, index = nested_data_to_arrays(
  File "C:\Users\DANISH LAPTOP\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 520, in nested_data_to_arrays
    arrays, columns = to_arrays(data, columns, dtype=dtype)
  File "C:\Users\DANISH LAPTOP\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 845, in to_arrays
    content, columns = _finalize_columns_and_data(arr, columns, dtype)
  File "C:\Users\DANISH LAPTOP\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\internals\construction.py", line 942, in _finalize_columns_and_data
    raise ValueError(err) from err
ValueError: 2 columns passed, passed data had 3 columns

= RESTART: C:\Users\DANISH LAPTOP\Downloads\FASDH25-portfolio2\scripts\regex_script_mubashir_alizain_iqra.py.py
gaza:
2023-10:4168
2023-11:4527
2023-12:2863
2024-01:1956
2024-02:1882
2024-03:2197
2024-04:993
gaza strip:
2023-10:4168
2023-11:4527
2023-12:2863
2024-01:1956
2024-02:1882
2024-03:2197
2024-04:993
gaza city:
2023-10:4174
2023-11:4529
2023-12:2865
2024-01:1956
2024-02:1882
2024-03:2199
2024-04:993
rafah:
2023-10:182
2023-11:150
2023-12:201
2024-01:41
2024-02:497
2024-03:253
2024-04:81
bayt lahya:
2023-10:11
2023-11:14
2023-12:8
2024-01:2
2024-02:3
2024-03:1
2024-04:2
jabalya:
2023-10:37
2023-11:103
2023-12:46
2024-01:12
2024-02:7
2024-03:8
2024-04:3
jabalia:
2023-10:33
2023-11:102
2023-12:44
2024-01:12
2024-02:7
2024-03:8
2024-04:2
bayt hanun:
2023-10:19
2023-11:17
2023-12:4
2024-01:1
2024-02:3
2024-03:7
2024-04:10
al-shifa hospital:
2023-10:31
2023-11:242
2023-12:23
2024-01:3
2024-02:15
2024-03:32
2024-04:13
khan younis:
2023-10:74
2023-11:132
2023-12:173
2024-01:74
2024-02:63
2024-03:40
2024-04:25
tunis:
2023-10:3
2023-11:4
2023-12:1
al burayj:
2023-10:3
2023-11:15
2023-12:17
2024-01:5
2024-02:2
2024-03:5
bureij:
2023-10:3
2023-11:15
2023-12:17
2024-01:5
2024-02:2
2024-03:5
remal:
2023-10:14
2023-11:3
2023-12:5
2024-03:3
2024-04:2
deir el-balah:
2023-10:38
2023-11:51
2023-12:45
2024-01:19
2024-02:31
2024-03:30
2024-04:12
an nusayrat:
2023-10:22
2023-11:16
2023-12:26
2024-01:11
2024-02:6
2024-03:9
2024-04:8
nuseirat:
2023-10:22
2023-11:16
2023-12:26
2024-01:11
2024-02:6
2024-03:9
2024-04:8
maghazi:
2023-10:15
2023-11:28
2023-12:49
2024-01:9
2024-02:2
2024-03:3
abu sittah:
2023-10:1
2023-12:4
2024-04:4
hijazi:
2023-10:2
2023-11:2
2023-12:1
2024-01:1
2024-04:2
bani suhayla:
2023-10:1
2023-11:1
2023-12:1
2024-01:2
abasan al kabirah:
2023-10:4
2023-11:5
2023-12:4
2024-02:1
az-zawayda:
2023-10:1
2023-12:1
2024-02:1
2024-04:1
shokat as-sufi:
2023-10:1
al-mughraqa:
2023-10:1
2024-01:1
abasan al-saghira:
2023-10:1
2023-11:2
qizan:
2023-10:1
al-azhar university:
2023-10:2
2023-11:1
2023-12:2
2024-01:1
al-aqsa university:
2023-10:1
2024-01:2
2024-02:2
bani suhela:
2023-10:3
2023-11:5
2024-03:2
al qararah:
2023-11:1
2024-01:1
2024-03:1
an nasr:
2024-01:1
al mawasi:
2024-01:1
2024-03:1
al amal:
2024-01:1
2024-03:1
al mu'askar:
2024-01:1
markaz al madinah:
2024-01:1
hamadah:
2024-02:1
Traceback (most recent call last):
  File "C:\Users\DANISH LAPTOP\Downloads\FASDH25-portfolio2\scripts\regex_script_mubashir_alizain_iqra.py.py", line 90, in <module>
    df.sort_values(by =["asciiname", "month"], inplace = True)
  File "C:\Users\DANISH LAPTOP\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 7172, in sort_values
    keys = [self._get_label_or_level_values(x, axis=axis) for x in by]
  File "C:\Users\DANISH LAPTOP\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py", line 1911, in _get_label_or_level_values
    raise KeyError(key)
KeyError: 'month'

= RESTART: C:\Users\DANISH LAPTOP\Downloads\FASDH25-portfolio2\scripts\regex_script_mubashir_alizain_iqra.py.py
gaza:
2023-10:4168
2023-11:4527
2023-12:2863
2024-01:1956
2024-02:1882
2024-03:2197
2024-04:993
gaza strip:
2023-10:4168
2023-11:4527
2023-12:2863
2024-01:1956
2024-02:1882
2024-03:2197
2024-04:993
gaza city:
2023-10:4174
2023-11:4529
2023-12:2865
2024-01:1956
2024-02:1882
2024-03:2199
2024-04:993
rafah:
2023-10:182
2023-11:150
2023-12:201
2024-01:41
2024-02:497
2024-03:253
2024-04:81
bayt lahya:
2023-10:11
2023-11:14
2023-12:8
2024-01:2
2024-02:3
2024-03:1
2024-04:2
jabalya:
2023-10:37
2023-11:103
2023-12:46
2024-01:12
2024-02:7
2024-03:8
2024-04:3
jabalia:
2023-10:33
2023-11:102
2023-12:44
2024-01:12
2024-02:7
2024-03:8
2024-04:2
bayt hanun:
2023-10:19
2023-11:17
2023-12:4
2024-01:1
2024-02:3
2024-03:7
2024-04:10
al-shifa hospital:
2023-10:31
2023-11:242
2023-12:23
2024-01:3
2024-02:15
2024-03:32
2024-04:13
khan younis:
2023-10:74
2023-11:132
2023-12:173
2024-01:74
2024-02:63
2024-03:40
2024-04:25
tunis:
2023-10:3
2023-11:4
2023-12:1
al burayj:
2023-10:3
2023-11:15
2023-12:17
2024-01:5
2024-02:2
2024-03:5
bureij:
2023-10:3
2023-11:15
2023-12:17
2024-01:5
2024-02:2
2024-03:5
remal:
2023-10:14
2023-11:3
2023-12:5
2024-03:3
2024-04:2
deir el-balah:
2023-10:38
2023-11:51
2023-12:45
2024-01:19
2024-02:31
2024-03:30
2024-04:12
an nusayrat:
2023-10:22
2023-11:16
2023-12:26
2024-01:11
2024-02:6
2024-03:9
2024-04:8
nuseirat:
2023-10:22
2023-11:16
2023-12:26
2024-01:11
2024-02:6
2024-03:9
2024-04:8
maghazi:
2023-10:15
2023-11:28
2023-12:49
2024-01:9
2024-02:2
2024-03:3
abu sittah:
2023-10:1
2023-12:4
2024-04:4
hijazi:
2023-10:2
2023-11:2
2023-12:1
2024-01:1
2024-04:2
bani suhayla:
2023-10:1
2023-11:1
2023-12:1
2024-01:2
abasan al kabirah:
2023-10:4
2023-11:5
2023-12:4
2024-02:1
az-zawayda:
2023-10:1
2023-12:1
2024-02:1
2024-04:1
shokat as-sufi:
2023-10:1
al-mughraqa:
2023-10:1
2024-01:1
abasan al-saghira:
2023-10:1
2023-11:2
qizan:
2023-10:1
al-azhar university:
2023-10:2
2023-11:1
2023-12:2
2024-01:1
al-aqsa university:
2023-10:1
2024-01:2
2024-02:2
bani suhela:
2023-10:3
2023-11:5
2024-03:2
al qararah:
2023-11:1
2024-01:1
2024-03:1
an nasr:
2024-01:1
al mawasi:
2024-01:1
2024-03:1
al amal:
2024-01:1
2024-03:1
al mu'askar:
2024-01:1
markaz al madinah:
2024-01:1
hamadah:
2024-02:1
Traceback (most recent call last):
  File "C:\Users\DANISH LAPTOP\Downloads\FASDH25-portfolio2\scripts\regex_script_mubashir_alizain_iqra.py.py", line 90, in <module>
    df.sort_values(by =["location", "month"], inplace = True)
  File "C:\Users\DANISH LAPTOP\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 7172, in sort_values
    keys = [self._get_label_or_level_values(x, axis=axis) for x in by]
  File "C:\Users\DANISH LAPTOP\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py", line 1911, in _get_label_or_level_values
    raise KeyError(key)
KeyError: 'location'

= RESTART: C:\Users\DANISH LAPTOP\Downloads\FASDH25-portfolio2\scripts\regex_script_mubashir_alizain_iqra.py.py
gaza:
2023-10:4168
2023-11:4527
2023-12:2863
2024-01:1956
2024-02:1882
2024-03:2197
2024-04:993
gaza strip:
2023-10:4168
2023-11:4527
2023-12:2863
2024-01:1956
2024-02:1882
2024-03:2197
2024-04:993
gaza city:
2023-10:4174
2023-11:4529
2023-12:2865
2024-01:1956
2024-02:1882
2024-03:2199
2024-04:993
rafah:
2023-10:182
2023-11:150
2023-12:201
2024-01:41
2024-02:497
2024-03:253
2024-04:81
bayt lahya:
2023-10:11
2023-11:14
2023-12:8
2024-01:2
2024-02:3
2024-03:1
2024-04:2
jabalya:
2023-10:37
2023-11:103
2023-12:46
2024-01:12
2024-02:7
2024-03:8
2024-04:3
jabalia:
2023-10:33
2023-11:102
2023-12:44
2024-01:12
2024-02:7
2024-03:8
2024-04:2
bayt hanun:
2023-10:19
2023-11:17
2023-12:4
2024-01:1
2024-02:3
2024-03:7
2024-04:10
al-shifa hospital:
2023-10:31
2023-11:242
2023-12:23
2024-01:3
2024-02:15
2024-03:32
2024-04:13
khan younis:
2023-10:74
2023-11:132
2023-12:173
2024-01:74
2024-02:63
2024-03:40
2024-04:25
tunis:
2023-10:3
2023-11:4
2023-12:1
al burayj:
2023-10:3
2023-11:15
2023-12:17
2024-01:5
2024-02:2
2024-03:5
bureij:
2023-10:3
2023-11:15
2023-12:17
2024-01:5
2024-02:2
2024-03:5
remal:
2023-10:14
2023-11:3
2023-12:5
2024-03:3
2024-04:2
deir el-balah:
2023-10:38
2023-11:51
2023-12:45
2024-01:19
2024-02:31
2024-03:30
2024-04:12
an nusayrat:
2023-10:22
2023-11:16
2023-12:26
2024-01:11
2024-02:6
2024-03:9
2024-04:8
nuseirat:
2023-10:22
2023-11:16
2023-12:26
2024-01:11
2024-02:6
2024-03:9
2024-04:8
maghazi:
2023-10:15
2023-11:28
2023-12:49
2024-01:9
2024-02:2
2024-03:3
abu sittah:
2023-10:1
2023-12:4
2024-04:4
hijazi:
2023-10:2
2023-11:2
2023-12:1
2024-01:1
2024-04:2
bani suhayla:
2023-10:1
2023-11:1
2023-12:1
2024-01:2
abasan al kabirah:
2023-10:4
2023-11:5
2023-12:4
2024-02:1
az-zawayda:
2023-10:1
2023-12:1
2024-02:1
2024-04:1
shokat as-sufi:
2023-10:1
al-mughraqa:
2023-10:1
2024-01:1
abasan al-saghira:
2023-10:1
2023-11:2
qizan:
2023-10:1
al-azhar university:
2023-10:2
2023-11:1
2023-12:2
2024-01:1
al-aqsa university:
2023-10:1
2024-01:2
2024-02:2
bani suhela:
2023-10:3
2023-11:5
2024-03:2
al qararah:
2023-11:1
2024-01:1
2024-03:1
an nasr:
2024-01:1
al mawasi:
2024-01:1
2024-03:1
al amal:
2024-01:1
2024-03:1
al mu'askar:
2024-01:1
markaz al madinah:
2024-01:1
hamadah:
2024-02:1
Traceback (most recent call last):
  File "C:\Users\DANISH LAPTOP\Downloads\FASDH25-portfolio2\scripts\regex_script_mubashir_alizain_iqra.py.py", line 90, in <module>
    df.sort_values(by =["asciiname", "month"], inplace = True)
  File "C:\Users\DANISH LAPTOP\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 7172, in sort_values
    keys = [self._get_label_or_level_values(x, axis=axis) for x in by]
  File "C:\Users\DANISH LAPTOP\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py", line 1911, in _get_label_or_level_values
    raise KeyError(key)
KeyError: 'month'

= RESTART: C:\Users\DANISH LAPTOP\Downloads\FASDH25-portfolio2\scripts\regex_script_mubashir_alizain_iqra.py.py
gaza:
2023-10:4168
2023-11:4527
2023-12:2863
2024-01:1956
2024-02:1882
2024-03:2197
2024-04:993
gaza strip:
2023-10:4168
2023-11:4527
2023-12:2863
2024-01:1956
2024-02:1882
2024-03:2197
2024-04:993
gaza city:
2023-10:4174
2023-11:4529
2023-12:2865
2024-01:1956
2024-02:1882
2024-03:2199
2024-04:993
rafah:
2023-10:182
2023-11:150
2023-12:201
2024-01:41
2024-02:497
2024-03:253
2024-04:81
bayt lahya:
2023-10:11
2023-11:14
2023-12:8
2024-01:2
2024-02:3
2024-03:1
2024-04:2
jabalya:
2023-10:37
2023-11:103
2023-12:46
2024-01:12
2024-02:7
2024-03:8
2024-04:3
jabalia:
2023-10:33
2023-11:102
2023-12:44
2024-01:12
2024-02:7
2024-03:8
2024-04:2
bayt hanun:
2023-10:19
2023-11:17
2023-12:4
2024-01:1
2024-02:3
2024-03:7
2024-04:10
al-shifa hospital:
2023-10:31
2023-11:242
2023-12:23
2024-01:3
2024-02:15
2024-03:32
2024-04:13
khan younis:
2023-10:74
2023-11:132
2023-12:173
2024-01:74
2024-02:63
2024-03:40
2024-04:25
tunis:
2023-10:3
2023-11:4
2023-12:1
al burayj:
2023-10:3
2023-11:15
2023-12:17
2024-01:5
2024-02:2
2024-03:5
bureij:
2023-10:3
2023-11:15
2023-12:17
2024-01:5
2024-02:2
2024-03:5
remal:
2023-10:14
2023-11:3
2023-12:5
2024-03:3
2024-04:2
deir el-balah:
2023-10:38
2023-11:51
2023-12:45
2024-01:19
2024-02:31
2024-03:30
2024-04:12
an nusayrat:
2023-10:22
2023-11:16
2023-12:26
2024-01:11
2024-02:6
2024-03:9
2024-04:8
nuseirat:
2023-10:22
2023-11:16
2023-12:26
2024-01:11
2024-02:6
2024-03:9
2024-04:8
maghazi:
2023-10:15
2023-11:28
2023-12:49
2024-01:9
2024-02:2
2024-03:3
abu sittah:
2023-10:1
2023-12:4
2024-04:4
hijazi:
2023-10:2
2023-11:2
2023-12:1
2024-01:1
2024-04:2
bani suhayla:
2023-10:1
2023-11:1
2023-12:1
2024-01:2
abasan al kabirah:
2023-10:4
2023-11:5
2023-12:4
2024-02:1
az-zawayda:
2023-10:1
2023-12:1
2024-02:1
2024-04:1
shokat as-sufi:
2023-10:1
al-mughraqa:
2023-10:1
2024-01:1
abasan al-saghira:
2023-10:1
2023-11:2
qizan:
2023-10:1
al-azhar university:
2023-10:2
2023-11:1
2023-12:2
2024-01:1
al-aqsa university:
2023-10:1
2024-01:2
2024-02:2
bani suhela:
2023-10:3
2023-11:5
2024-03:2
al qararah:
2023-11:1
2024-01:1
2024-03:1
an nasr:
2024-01:1
al mawasi:
2024-01:1
2024-03:1
al amal:
2024-01:1
2024-03:1
al mu'askar:
2024-01:1
markaz al madinah:
2024-01:1
hamadah:
2024-02:1
