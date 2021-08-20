from experiments.diceExperiment import diceExperiment


Ntries = 200000
sides = 20
side = 4
experiment = diceExperiment(Ntries,sides)
print('Probability of throwing a dice with ' + str(sides) + ' and result in ' + str(side) + ' is : ' + str(experiment.getProbability(side)*100) + '%')
