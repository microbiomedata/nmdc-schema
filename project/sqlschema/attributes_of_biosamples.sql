

CREATE TABLE "Biosample" (
	id TEXT NOT NULL, 
	depth TEXT, 
	intval INTEGER NOT NULL, 
	sometimes_absent TEXT NOT NULL, 
	lat FLOAT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Collection" (
	biosamples TEXT, 
	meetings TEXT, 
	PRIMARY KEY (biosamples, meetings)
);

CREATE TABLE "Meeting" (
	id TEXT NOT NULL, 
	meeting_info VARCHAR(5), 
	PRIMARY KEY (id)
);
