CREATE TABLE users(
	email VARCHAR(255) PRIMARY KEY,
	created_at TIMESTAMP DEFAULT NOW()
);

#Find earliest date a user joined
SELECT
	DATE_FORMAT(created_at,'%M %D %Y') AS earliest_date
FROM users
ORDER BY created_at
LIMIT 1;

#Find email of the first (earliest) user
SELECT
	email,
	created_at
FROM users
ORDER BY created_at
LIMIT 1;
# sau cu SubQuery
SELECT 
	*
FROM users
WHERE created_at=(SELECT MIN(created_at) FROM users);


#Users according to the month they joined
SELECT
	DATE_FORMAT(created_at,'%M') AS month,
	COUNT(*) AS count
FROM users
GROUP BY DATE_FORMAT(created_at,'%M')	
ORDER BY COUNT DESC;

#Count number of users with yahoo email
SELECT
	COUNT(*) AS yahoo_users
FROM users
WHERE email LIKE '%@yahoo.com';

#Calculate total number of users from each email host

SELECT
	CASE
		WHEN email LIKE '%gmail.com' THEN 'gmail'
		WHEN email LIKE '%yahoo.com' THEN 'yahoo'
		WHEN email LIKE '%hotmail.com' THEN 'hotmail'
		ELSE 'other'
	END AS provider,
	COUNT(*) AS total_users
FROM users
GROUP BY provider;
