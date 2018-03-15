import pprint, os, time
import numpy as np, tellurium as te

# level and version of SBML to use
lv_string = 'l3v1'
# run all supported test cases
cases = te.getSupportedTestCases(0,980)
print('Using the following {} cases:'.format(len(cases)))
pprint.PrettyPrinter().pprint(cases)
# maximum cutoff for passing a test case (per-variable)
max_threshold = 1e-3

lv_archive_path = os.path.join('archives', lv_string)
n_failures = 0
n_successes = 0
diffs = np.zeros(len(cases))

te.disablePlotting()

# start time
t0 = time.time()

for k,case in enumerate(cases):
    archive_name = case+'.omex'
    print('Running {}'.format(archive_name))
    case_path = os.path.join(lv_archive_path, archive_name)
    te.convertAndExecuteCombineArchive(case_path)
    
    # compare results
    csv = te.extractFileFromCombineArchive(case_path, case+'-results.csv')
    from io import StringIO
    import pandas as pd
    df = pd.read_csv(StringIO(csv))
    report = te.getLastReport()
    report = report.drop(report.shape[0]-1)
    df.columns = report.columns
    # difference between simulation and expected results
    diff = report.subtract(df)
    max_val = (diff**2).mean().max()
    diffs[k] = max_val
    if max_val > max_threshold:
        n_failures += 1
    else:
        n_successes += 1

# finish time
t1 = time.time()
        
print('Finished running tests: {} PASS, {} FAIL'.format(n_successes, n_failures))
print('Median of divergence: {}'.format(np.median(diffs)))
print('Max divergence: {}'.format(diffs.max()))
print('Total run time: {}'.format(t1-t0))
