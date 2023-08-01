# RFM Analysis
RFM analysis is a common tool used among the sector to segment their donors.
RFM allows fundraisers to target specific clusters of donors with communications that are much more relevant for their particular behavior – and thus generate much higher rates of response, plus increased loyalty and donor lifetime value. Like other segmentation methods, an RFM model is a powerful way to identify groups of donors for special treatment.

## Recency, Frequency, and Monetary
- Recency: How much time has elapsed since a donors last donation?
- Frequency: How often has a donor donated during a particular period of time?
- Monetary: Also referred to as “monetary value,” this factor reflects how much a donor has given.

## Calculating RFM
1. The first step in building an RFM model is to assign Recency, Frequency and Monetary values to each donor. The raw data will be provided to you in the assignment.

- Recency is calculated as the amount of time since the customer’s most recent donation
- Frequency is the total number of donations made by a donor
- Monetary is the total amount that the donor has given across all transactions (during a defined period).

2. The second step is to divide the customer list into tiered groups for each of the three dimensions (R, F and M)


| Recency                 | Frequency                 | Monetary                       |
|-------------------------|---------------------------|--------------------------------|
| R-Teir-1 (most recent)  | F-Teir-1 (most frequent)  | M-Teir-1 (highest total spend) |
| R-Teir-2   | F-Teir-1 (most frequent)  | M-Teir-1 (highest total spend) |
| R-Teir-1 (most recent)  | F-Teir-1 (most frequent)  | M-Teir-1 (highest total spend) |
| R-Teir-1 (least recent) | F-Teir-1 (least frequent) | M-Teir-4 (lowest total spend)  |


This results in 64 distinct customer segments (4x4x4), into which donors will be segmented

# Assignment
Using the sample data provided, implement RFM segmentation in python with unit tests.

- You may decide on the data structure you would like to use for the inputs and outputs for the `rfm` function.
- You may use any packages, libraries, you'd like.
- You may use google but please try to implement the solution on your own. I'm more interested in seeing how you think rather than you creating a perfect solution.
