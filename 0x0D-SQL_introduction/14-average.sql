-- MySql Script By Phoenix
-- Computes average of scores fields in second_table
SELECT SUM(score)/COUNT(score) AS average FROM second_table;
