

groupPlot = {}

groupPlot['Fake']  = {
                  'nameHR' : 'nonprompt',
                  'isSignal' : 0,
                  'color': 921,    # kGray + 1
                  'samples'  : ['Fake_m', 'Fake_e']
}

groupPlot['top']  = {  
                  'nameHR' : 'tW and t#bar{t}',
                  'isSignal' : 0,
                  #'color': 400,   # kYellow
                  'color': ROOT.kYellow,   # kYellow
                  'samples'  : ['top']
              }

_bins = [30, 50, 70, 100, 130, 160, 200, 250, 300, 350, 400, 500, 700]
dys = {}
for i in range(-1, len(_bins)-1):
    if i == -1:
        # underflow bin
        dys[f'DY{i+1}'] = f'(ptll < {_bins[i+1]})'
    elif i == len(_bins)-2:
        # overflow bin
        dys[f'DY{i+1}'] = f'(ptll >= {_bins[i]})'
    else:
        dys[f'DY{i+1}'] = f'(ptll >= {_bins[i]} && ptll < {_bins[i+1]})'

_i = 0
for dy in dys.keys():
    groupPlot[dy] = {
            'nameHR': dy,
            'isSignal': 0,
            'color': ROOT.kGreen - 7 + _i,
            'samples': ['DY_' + dy]
            }
    _i +=1


"""
groupPlot['DY']  = {  
                  'nameHR' : ,
                  'isSignal' : 0,
                  #'color': 418,    # kGreen+2
                  'color': ROOT.kGreen+2,    # kGreen+2
                  'samples'  : ['DY_hardJets']
              }
groupPlot['DY_PUJets']  = {  
                  'nameHR' : "DY 1 PU jet",
                  'isSignal' : 0,
                  'color': 416,    # kGreen
                  'samples'  : ['DY_PUJets']
              }
"""


groupPlot['Multiboson']  = {  
                  'nameHR' : 'Multiboson',
                  'isSignal' : 0,
                  'color': 617, # kViolet + 1  
                  #'samples'  : ['WWewk','WW', 'ggWW', 'VVV', 'VZ', 'WZ', 'ZZ', 'Vg', 'Wg', 'VgS_H', 'VgS_L']
                  'samples'  : ['WWewk','WW', 'ggWW', 'Vg', 'VgS_H', 'VgS_L', 'VZ', 'VVV']
                  #'VVV', 'VZ', 'WZ', 'ZZ', 'Vg', 'Wg', 'VgS_H', 'VgS_L']
              }

groupPlot['Zjj']  = {  
                  'nameHR': 'Zjj',
                  'isSignal' : 1,
                  'color': 600,    # kBlue
                  'samples'    : ['Zjj']
              }

groupPlot['DATA']  = { 
                  'nameHR' : 'Data',
                  'color': 1 ,  
                  'isSignal' : 0,
                  'isData'   : 1 ,
                  'isBlind'  : 0
              }