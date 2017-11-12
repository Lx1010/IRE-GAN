# NEWS Recommendation Using Generative adversarial neural network.

## Problem Statement
NEWS Recommendation using GAN networks which has two neural nets (i) generative (ii) discriminative.

## ABSTRACT
In IRGAN for NEWS Recommendation, the generative retrieval focusing on predicting relevant documents given a query. while the discriminative retrieval focusing on predicting relevancy given a query-document pair. 

The discriminative model, provides guidance to train the generative model towards fitting the underlying relevance distribution over documents given the query. 

The generative model, acting as an attacker to the current discriminative model, generates diffcult examples for the discriminative model in an adversarial way by minimising its discrimination objective.

## overall objective function 

![overall](https://user-images.githubusercontent.com/8746899/32701426-2cf50f72-c7fb-11e7-8e69-68345c2e7685.png)

![score_gen](https://user-images.githubusercontent.com/8746899/32701591-ac42dda6-c7fe-11e7-9fd5-3fea76571d1c.png)

The above snapshot is about overall objective to implement

## Generative retrieval model:
Pθ(d|q,r), which tries to generate(or select) relevant documents, from the candidate pool for the given query q goal is to approximate the true relevance distribution over documents Ptrue(d|q,r) as much as possible.

![gen](https://user-images.githubusercontent.com/8746899/32701565-2fde2d1a-c7fe-11e7-8b5b-61bb94357287.png)

## Discriminative retrieval model :
fφ(q, d), which, in contrary, tries to discriminate well-matched query-document tuples (q, d) from ill-matched ones, where the goodness of matching given by fφ(q, d) depends on the relevance of d to q.

In other words, its goal is to distinguish between relevant documents and non-relevant documents for the query q as accurately as possible. 

![dis](https://user-images.githubusercontent.com/8746899/32701580-7db49880-c7fe-11e7-82e9-8b3fb8f521f5.png)

## Algo for IRGAN
![algo](https://user-images.githubusercontent.com/8746899/32701603-cf7d353c-c7fe-11e7-9d0f-990c4bee3375.png)

## Data Generation

The data dump consists of user_id and set of article_id which represent the documents that the user read.

Each sample is a tuple of the form

<user_id>  <article_id> <label>

Only those users were taken who read >=10 articles, The ratio for read article to unread articles was 10:3

### Technique used: 

Matrix Factorization

### User and article Representation

Every user and article is represented as a 5 dimensional vector.

### Scoring Function

1) Dot product:

	s (u, i) = dot(u,i) +item_bias


2) Element-wise Multiplication

	s (u, i) = element_wise_multiply(u,i)


Neural layer added above elementwise multiplicated vector to get a score.
Activation used: softmax

## results

![833](https://user-images.githubusercontent.com/8746899/32701756-205adbec-c801-11e7-992e-5c7c968b2d63.png)


### performance

element wise product - 8.877%

dot product - 8.827%.

## To run the code

run "python cf_gan_element.py" for element wise product scoring function

run "python cf_gan_dot.py" for dot product scoring function
