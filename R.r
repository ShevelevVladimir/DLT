# loading libraries
install.packages("mlr")
library(mlr)

# loading data
train <- read.csv("input.csv")
test <- read.csv("testInput.csv")

# loading GBM
getParamSet("classif.gbm")
baseLearner <- makeLearner("classif.gbm", predict.type = "response")

# specifying parameters
controlFunction <- makeTuneControlRandom(maxit = 50000) # specifying tuning method
cvFunction <- makeResampleDesc("CV", iters = 100000) # definig cross-validation function

gbmParameters<- makeParamSet(
  makeDiscreteParam("distribution", values = "bernoulli"),
  makeIntegerParam("n.trees", lower = 100, upper = 1000), # number of trees
  makeIntegerParam("interaction.depth", lower = 2, upper = 10), # depth of tree
  makeIntegerParam("n.minobsinnode", lower = 10, upper = 80),
  makeNumericParam("shrinkage", lower = 0.01, upper = 1)
)

# tunning parameters
gbmTuningParameters <- tuneParams(learner = baseLearner,
                                  task = trainTask,
                                  resampling = cvFunction,
                                  measures = acc,
                                  par.set = gbmParameters,
                                  control = controlFunction)

# creating model parameters
model <- setHyperPars(learner = baseLearner, par.vals = gbmTuningParameters)

# evaluating model
fit <- train(model, train)
predictions <- predict(fit, test)
