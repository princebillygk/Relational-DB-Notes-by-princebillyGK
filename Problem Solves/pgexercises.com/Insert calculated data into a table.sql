INSERT INTO cd.facilities (
	SELECT max(facid) + 1, 'Spa', 20, 30, 100000, 800 FROM cd.facilities);
