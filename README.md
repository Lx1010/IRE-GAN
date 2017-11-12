# NEWS Recommendation Using Generative adversarial neural network.

## Problem Statement
NEWS Recommendation using GAN networks which has two neural nets (i) generative (ii) discriminative.

## ABSTRACT
In IRGAN for NEWS Recommendation, the generative retrieval focusing on predicting relevant documents given a query. while the discriminative retrieval focusing on predicting relevancy given a query-document pair. 

On one hand, the discriminative model, aiming to mine signals from labelled data, provides guidance to train the generative model towards fitting the underlying relevance distribution over documents given the query. On the other hand, the generative model, acting as an attacker to the current discriminative model, generates diffcult examples for the discriminative model in an adversarial way by minimising its discrimination objective.

With the competition between these two models:(I) generative model learns to fit the relevance distribution over documents via the signals from the discriminative model, and (ii) discriminative model is able to exploit the unlabelled data selected by the generative model to achieve a better estimation for document ranking.

## Generative retrieval model:
Pθ(d|q,r), which tries to generate(or select) relevant documents, from the candidate pool for the given query q goal is to approximate the true relevance distribution over documents Ptrue(d|q,r) as much as possible.

## Discriminative retrieval model :
fφ(q, d), which, in contrary, tries to discriminate well-matched query-document tuples (q, d) from ill-matched ones, where the goodness of matching given by fφ(q, d) depends on the relevance of d to q.

In other words, its goal is to distinguish between relevant documents and non-relevant documents for the query q as accurately as possible. 
