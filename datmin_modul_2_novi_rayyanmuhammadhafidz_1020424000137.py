KeyError: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).
Traceback:
File "/mount/src/datmin---dashboard/datmin_modul_2_novi_rayyanmuhammadhafidz_1020424000137.py", line 83, in <module>
    df_fixed = df.apply(fix_health_data, axis=1)
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/core/frame.py", line 12435, in apply
    return op.apply().__finalize__(self, method="apply")
           ~~~~~~~~^^
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/core/apply.py", line 1015, in apply
    return self.apply_standard()
           ~~~~~~~~~~~~~~~~~~~^^
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/core/apply.py", line 1167, in apply_standard
    results, res_index = self.apply_series_generator()
                         ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/core/apply.py", line 1183, in apply_series_generator
    results[i] = self.func(v, *self.args, **self.kwargs)
                 ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/mount/src/datmin---dashboard/datmin_modul_2_novi_rayyanmuhammadhafidz_1020424000137.py", line 58, in fix_health_data
    if row['HbA1c'] > 20:
       ~~~^^^^^^^^^
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/core/series.py", line 959, in __getitem__
    return self._get_value(key)
           ~~~~~~~~~~~~~~~^^^^^
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/core/series.py", line 1046, in _get_value
    loc = self.index.get_loc(label)
File "/home/adminuser/venv/lib/python3.14/site-packages/pandas/core/indexes/base.py", line 3648, in get_loc
    raise KeyError(key) from err