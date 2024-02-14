-- MySql Script By Phoenix
-- Scripts that lists number of records with same score
SELECT score, COUNT(*) AS number FROM second_table Group BY score;
