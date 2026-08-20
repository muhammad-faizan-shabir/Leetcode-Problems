/* Write your T-SQL query statement below */
SELECT t.tweet_id
FROM Tweets as t
WHERE LEN(t.content) > 15;