# NEWS Recommendation Using Generative adversarial neural network.

## Problem Statement

NEWS Recommendation using GAN networks
GAN has two networks (i) generative (ii) discriminative neural networks.

## Abstract
In GAN, One neural net takes noise as input and generates samples and so is called the generator. The other model, called the discriminator receives samples from both the generator and the training data, and has to be able to distinguish between the two sources. These two networks play a continuous game, where the generator is learning to produce more and more realistic samples, and the discriminator is learning to get better and better at distinguishing generated data from real data. These two networks are trained simultaneously.

As we are using IRGAN for NEWS Recommendation, the generative
retrieval focusing on predicting relevant documents given a query. while
the discriminative retrieval focusing on predicting relevancy given a
query-document pair. 

On one hand, the discriminative model, aiming to
mine signals from labelled data, provides guidance to train the generative
model towards fitting the underlying relevance distribution over
documents given the query. On the other hand, the generative model,
acting as an attacker to the current discriminative model, generates
diffcult examples for the discriminative model in an adversarial way by
minimising its discrimination objective.

With the competition between these two models:(I) generative model
learns to fitthe relevance distribution over documents via the signals from
the discriminative model, and (ii) discriminative model is able to exploit
the unlabelled data selected by the generative model to achieve a better
estimation for document ranking.

## Performance
8.877% for additional layer on element wise product of
scoring function. And 8.827% for dot product.

## INTRODUCTION
We have a set of queries {q1,...,qN} and a set of documents{d1,...,dM},
where queries here is number of readers and documents are set of articles
read by those readers.
### Overall Objective
Thus, inspired by the idea of GAN, we aim to unify these two different
types of IR models by letting them play a minimax game: the generative
retrieval model would try to generate (or select) relevant documents that
look like the ground-truth relevant documents and therefore could fool
the discriminative retrieval model, whereas the discriminative retrieval
model would try to draw a clear distinction between the ground-truth
relevant documents and the generated ones made by its opponent
generative retrieval model. Formally, we have:

