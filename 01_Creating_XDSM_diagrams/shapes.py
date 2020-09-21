from pyxdsm.XDSM import XDSM

# Define styles
OPT = "Optimization"
SUBOPT = "SubOptimization"
SOLVER = "MDA"
DOE = "DOE"
IFUNC = "ImplicitFunction"
FUNC = "Function"
GROUP = "Group"
IGROUP = "ImplicitGroup"
METAMODEL = "Metamodel"
DataIO ='DataIO'
DataInter ='DataInter'

# not avialable
icomp = 'ImplicitAnalysis'
ecomp = 'Analysis'



x = XDSM()

# create system 
#x.add_system('input',icomp, (r'\text{}',r'ImplicitAnalysis'))
#x.add_system('input',ecomp, (r'\text{}',r'Analysis'))
x.add_system('input',OPT, (r'\text{}',r'Optimization'))
x.add_system('input',SUBOPT, (r'\text{}',r'SubOptimization'))
x.add_system('input',SOLVER, (r'\text{}',r'MDA'))
x.add_system('input',DOE, (r'\text{}',r'DOE'))
x.add_system('input',IFUNC, (r'\text{}',r'ImplicitFunction'))
x.add_system('input',FUNC, (r'\text{}',r'Function'))
x.add_system('input',GROUP, (r'\text{}',r'Group'))
x.add_system('input',IGROUP, (r'\text{}',r'ImplicitGroup'))
x.add_system('input',METAMODEL, (r'\text{}',r'Metamodel'))


x.add_system('input',DataIO, (r'\text{}',r'DataIO'))
x.add_system('input',DataInter, (r'\text{}',r'DataInter'))



x.write('Xshapes')