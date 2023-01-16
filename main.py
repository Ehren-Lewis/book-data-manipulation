import pandas as pd

data = [
	{
		"Title": "Fundamentals of Wavelets",
		"Author": "\"Goswami",
		"Genre": " Jaideva\"",
		"SubGenre": "tech",
		"Height": "signal_processing",
		"Publisher": "228"
	},
	{
		"Title": "Data Smart",
		"Author": "\"Foreman",
		"Genre": " John\"",
		"SubGenre": "tech",
		"Height": "data_science",
		"Publisher": "235"
	},
	{
		"Title": "God Created the Integers",
		"Author": "\"Hawking",
		"Genre": " Stephen\"",
		"SubGenre": "tech",
		"Height": "mathematics",
		"Publisher": "197"
	},
	{
		"Title": "Superfreakonomics",
		"Author": "\"Dubner",
		"Genre": " Stephen\"",
		"SubGenre": "science",
		"Height": "economics",
		"Publisher": "179"
	},
	{
		"Title": "Orientalism",
		"Author": "\"Said",
		"Genre": " Edward\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "197"
	},
	{
		"Title": "\"Nature of Statistical Learning Theory",
		"Author": " The\"",
		"Genre": "\"Vapnik",
		"SubGenre": " Vladimir\"",
		"Height": "tech",
		"Publisher": "data_science"
	},
	{
		"Title": "Integration of the Indian States",
		"Author": "\"Menon",
		"Genre": " V P\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "217"
	},
	{
		"Title": "\"Drunkard's Walk",
		"Author": " The\"",
		"Genre": "\"Mlodinow",
		"SubGenre": " Leonard\"",
		"Height": "science",
		"Publisher": "mathematics"
	},
	{
		"Title": "Image Processing & Mathematical Morphology",
		"Author": "\"Shih",
		"Genre": " Frank\"",
		"SubGenre": "tech",
		"Height": "signal_processing",
		"Publisher": "241"
	},
	{
		"Title": "How to Think Like Sherlock Holmes",
		"Author": "\"Konnikova",
		"Genre": " Maria\"",
		"SubGenre": "nonfiction",
		"Height": "psychology",
		"Publisher": "240"
	},
	{
		"Title": "Data Scientists at Work",
		"Author": "Sebastian Gutierrez",
		"Genre": "tech",
		"SubGenre": "data_science",
		"Height": "230",
		"Publisher": "Apress"
	},
	{
		"Title": "Slaughterhouse Five",
		"Author": "\"Vonnegut",
		"Genre": " Kurt\"",
		"SubGenre": "fiction",
		"Height": "classic",
		"Publisher": "198"
	},
	{
		"Title": "Birth of a Theorem",
		"Author": "\"Villani",
		"Genre": " Cedric\"",
		"SubGenre": "science",
		"Height": "mathematics",
		"Publisher": "234"
	},
	{
		"Title": "Structure & Interpretation of Computer Programs",
		"Author": "\"Sussman",
		"Genre": " Gerald\"",
		"SubGenre": "tech",
		"Height": "computer_science",
		"Publisher": "240"
	},
	{
		"Title": "\"Age of Wrath",
		"Author": " The\"",
		"Genre": "\"Eraly",
		"SubGenre": " Abraham\"",
		"Height": "nonfiction",
		"Publisher": "history"
	},
	{
		"Title": "\"Trial",
		"Author": " The\"",
		"Genre": "\"Kafka",
		"SubGenre": " Frank\"",
		"Height": "fiction",
		"Publisher": "classic"
	},
	{
		"Title": "Statistical Decision Theory'",
		"Author": "\"Pratt",
		"Genre": " John\"",
		"SubGenre": "tech",
		"Height": "data_science",
		"Publisher": "236"
	},
	{
		"Title": "Data Mining Handbook",
		"Author": "\"Nisbet",
		"Genre": " Robert\"",
		"SubGenre": "tech",
		"Height": "data_science",
		"Publisher": "242"
	},
	{
		"Title": "\"New Machiavelli",
		"Author": " The\"",
		"Genre": "\"Wells",
		"SubGenre": " H. G.\"",
		"Height": "fiction",
		"Publisher": "novel"
	},
	{
		"Title": "Physics & Philosophy",
		"Author": "\"Heisenberg",
		"Genre": " Werner\"",
		"SubGenre": "philosophy",
		"Height": "science",
		"Publisher": "197"
	},
	{
		"Title": "Making Software",
		"Author": "\"Oram",
		"Genre": " Andy\"",
		"SubGenre": "tech",
		"Height": "computer_science",
		"Publisher": "232"
	},
	{
		"Title": "\"Analysis",
		"Author": " Vol I\"",
		"Genre": "\"Tao",
		"SubGenre": " Terence\"",
		"Height": "tech",
		"Publisher": "mathematics"
	},
	{
		"Title": "Machine Learning for Hackers",
		"Author": "\"Conway",
		"Genre": " Drew\"",
		"SubGenre": "tech",
		"Height": "data_science",
		"Publisher": "233"
	},
	{
		"Title": "\"Signal and the Noise",
		"Author": " The\"",
		"Genre": "\"Silver",
		"SubGenre": " Nate\"",
		"Height": "tech",
		"Publisher": "data_science"
	},
	{
		"Title": "Python for Data Analysis",
		"Author": "\"McKinney",
		"Genre": " Wes\"",
		"SubGenre": "tech",
		"Height": "data_science",
		"Publisher": "233"
	},
	{
		"Title": "Introduction to Algorithms",
		"Author": "\"Cormen",
		"Genre": " Thomas\"",
		"SubGenre": "tech",
		"Height": "computer_science",
		"Publisher": "234"
	},
	{
		"Title": "\"Beautiful and the Damned",
		"Author": " The\"",
		"Genre": "\"Deb",
		"SubGenre": " Siddhartha\"",
		"Height": "nonfiction",
		"Publisher": "history"
	},
	{
		"Title": "\"Outsider",
		"Author": " The\"",
		"Genre": "\"Camus",
		"SubGenre": " Albert\"",
		"Height": "fiction",
		"Publisher": "classic"
	},
	{
		"Title": "\"Complete Sherlock Holmes",
		"Author": " The - Vol I\"",
		"Genre": "\"Doyle",
		"SubGenre": " Arthur Conan\"",
		"Height": "fiction",
		"Publisher": "classic"
	},
	{
		"Title": "\"Complete Sherlock Holmes",
		"Author": " The - Vol II\"",
		"Genre": "\"Doyle",
		"SubGenre": " Arthur Conan\"",
		"Height": "fiction",
		"Publisher": "classic"
	},
	{
		"Title": "\"Wealth of Nations",
		"Author": " The\"",
		"Genre": "\"Smith",
		"SubGenre": " Adam\"",
		"Height": "science",
		"Publisher": "economics"
	},
	{
		"Title": "\"Pillars of the Earth",
		"Author": " The\"",
		"Genre": "\"Follett",
		"SubGenre": " Ken\"",
		"Height": "fiction",
		"Publisher": "novel"
	},
	{
		"Title": "Mein Kampf",
		"Author": "\"Hitler",
		"Genre": " Adolf\"",
		"SubGenre": "nonfiction",
		"Height": "autobiography",
		"Publisher": "212"
	},
	{
		"Title": "\"Tao of Physics",
		"Author": " The\"",
		"Genre": "\"Capra",
		"SubGenre": " Fritjof\"",
		"Height": "science",
		"Publisher": "physics"
	},
	{
		"Title": "Surely You're Joking Mr Feynman",
		"Author": "\"Feynman",
		"Genre": " Richard\"",
		"SubGenre": "science",
		"Height": "physics",
		"Publisher": "198"
	},
	{
		"Title": "\"Farewell to Arms",
		"Author": " A\"",
		"Genre": "\"Hemingway",
		"SubGenre": " Ernest\"",
		"Height": "fiction",
		"Publisher": "classic"
	},
	{
		"Title": "\"Veteran",
		"Author": " The\"",
		"Genre": "\"Forsyth",
		"SubGenre": " Frederick\"",
		"Height": "fiction",
		"Publisher": "novel"
	},
	{
		"Title": "False Impressions",
		"Author": "\"Archer",
		"Genre": " Jeffery\"",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "177"
	},
	{
		"Title": "\"Last Lecture",
		"Author": " The\"",
		"Genre": "\"Pausch",
		"SubGenre": " Randy\"",
		"Height": "nonfiction",
		"Publisher": "autobiography"
	},
	{
		"Title": "Return of the Primitive",
		"Author": "\"Rand",
		"Genre": " Ayn\"",
		"SubGenre": "philosophy",
		"Height": "objectivism",
		"Publisher": "202"
	},
	{
		"Title": "Jurassic Park",
		"Author": "\"Crichton",
		"Genre": " Michael\"",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "174"
	},
	{
		"Title": "\"Russian Journal",
		"Author": " A\"",
		"Genre": "\"Steinbeck",
		"SubGenre": " John\"",
		"Height": "nonfiction",
		"Publisher": "history"
	},
	{
		"Title": "Tales of Mystery and Imagination",
		"Author": "\"Poe",
		"Genre": " Edgar Allen\"",
		"SubGenre": "fiction",
		"Height": "classic",
		"Publisher": "172"
	},
	{
		"Title": "Freakonomics",
		"Author": "\"Dubner",
		"Genre": " Stephen\"",
		"SubGenre": "science",
		"Height": "economics",
		"Publisher": "197"
	},
	{
		"Title": "\"Hidden Connections",
		"Author": " The\"",
		"Genre": "\"Capra",
		"SubGenre": " Fritjof\"",
		"Height": "science",
		"Publisher": "physics"
	},
	{
		"Title": "\"Story of Philosophy",
		"Author": " The\"",
		"Genre": "\"Durant",
		"SubGenre": " Will\"",
		"Height": "philosophy",
		"Publisher": "history"
	},
	{
		"Title": "Asami Asami",
		"Author": "\"Deshpande",
		"Genre": " P L\"",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "205"
	},
	{
		"Title": "Journal of a Novel",
		"Author": "\"Steinbeck",
		"Genre": " John\"",
		"SubGenre": "fiction",
		"Height": "classic",
		"Publisher": "196"
	},
	{
		"Title": "Once There Was a War",
		"Author": "\"Steinbeck",
		"Genre": " John\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "196"
	},
	{
		"Title": "\"Moon is Down",
		"Author": " The\"",
		"Genre": "\"Steinbeck",
		"SubGenre": " John\"",
		"Height": "fiction",
		"Publisher": "classic"
	},
	{
		"Title": "\"Brethren",
		"Author": " The\"",
		"Genre": "\"Grisham",
		"SubGenre": " John\"",
		"Height": "fiction",
		"Publisher": "novel"
	},
	{
		"Title": "In a Free State",
		"Author": "\"Naipaul",
		"Genre": " V. S.\"",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "196"
	},
	{
		"Title": "Catch 22",
		"Author": "\"Heller",
		"Genre": " Joseph\"",
		"SubGenre": "fiction",
		"Height": "classic",
		"Publisher": "178"
	},
	{
		"Title": "\"Complete Mastermind",
		"Author": " The\"",
		"Genre": "BBC",
		"SubGenre": "nonfiction",
		"Height": "trivia",
		"Publisher": "178"
	},
	{
		"Title": "Dylan on Dylan",
		"Author": "\"Dylan",
		"Genre": " Bob\"",
		"SubGenre": "nonfiction",
		"Height": "autobiography",
		"Publisher": "197"
	},
	{
		"Title": "Soft Computing & Intelligent Systems",
		"Author": "\"Gupta",
		"Genre": " Madan\"",
		"SubGenre": "tech",
		"Height": "data_science",
		"Publisher": "242"
	},
	{
		"Title": "Textbook of Economic Theory",
		"Author": "\"Stonier",
		"Genre": " Alfred\"",
		"SubGenre": "tech",
		"Height": "economics",
		"Publisher": "242"
	},
	{
		"Title": "Econometric Analysis",
		"Author": "\"Greene",
		"Genre": " W. H.\"",
		"SubGenre": "tech",
		"Height": "economics",
		"Publisher": "242"
	},
	{
		"Title": "Learning OpenCV",
		"Author": "\"Bradsky",
		"Genre": " Gary\"",
		"SubGenre": "tech",
		"Height": "signal_processing",
		"Publisher": "232"
	},
	{
		"Title": "Data Structures Using C & C++",
		"Author": "\"Tanenbaum",
		"Genre": " Andrew\"",
		"SubGenre": "tech",
		"Height": "computer_science",
		"Publisher": "235"
	},
	{
		"Title": "\"Computer Vision",
		"Author": " A Modern Approach\"",
		"Genre": "\"Forsyth",
		"SubGenre": " David\"",
		"Height": "tech",
		"Publisher": "signal_processing"
	},
	{
		"Title": "Principles of Communication Systems",
		"Author": "\"Taub",
		"Genre": " Schilling\"",
		"SubGenre": "tech",
		"Height": "signal_processing",
		"Publisher": "240"
	},
	{
		"Title": "Let Us C",
		"Author": "\"Kanetkar",
		"Genre": " Yashwant\"",
		"SubGenre": "tech",
		"Height": "computer_science",
		"Publisher": "213"
	},
	{
		"Title": "\"Amulet of Samarkand",
		"Author": " The\"",
		"Genre": "\"Stroud",
		"SubGenre": " Jonathan\"",
		"Height": "fiction",
		"Publisher": "novel"
	},
	{
		"Title": "Crime and Punishment",
		"Author": "\"Dostoevsky",
		"Genre": " Fyodor\"",
		"SubGenre": "fiction",
		"Height": "classic",
		"Publisher": "180"
	},
	{
		"Title": "Angels & Demons",
		"Author": "\"Brown",
		"Genre": " Dan\"",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "178"
	},
	{
		"Title": "\"Argumentative Indian",
		"Author": " The\"",
		"Genre": "\"Sen",
		"SubGenre": " Amartya\"",
		"Height": "nonfiction",
		"Publisher": "history"
	},
	{
		"Title": "Sea of Poppies",
		"Author": "\"Ghosh",
		"Genre": " Amitav\"",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "197"
	},
	{
		"Title": "\"Idea of Justice",
		"Author": " The\"",
		"Genre": "\"Sen",
		"SubGenre": " Amartya\"",
		"Height": "philosophy",
		"Publisher": "economics"
	},
	{
		"Title": "\"Raisin in the Sun",
		"Author": " A\"",
		"Genre": "\"Hansberry",
		"SubGenre": " Lorraine\"",
		"Height": "fiction",
		"Publisher": "novel"
	},
	{
		"Title": "All the President's Men",
		"Author": "\"Woodward",
		"Genre": " Bob\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "177"
	},
	{
		"Title": "\"Prisoner of Birth",
		"Author": " A\"",
		"Genre": "\"Archer",
		"SubGenre": " Jeffery\"",
		"Height": "fiction",
		"Publisher": "novel"
	},
	{
		"Title": "Scoop!",
		"Author": "\"Nayar",
		"Genre": " Kuldip\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "216"
	},
	{
		"Title": "Ahe Manohar Tari",
		"Author": "\"Deshpande",
		"Genre": " Sunita\"",
		"SubGenre": "nonfiction",
		"Height": "autobiography",
		"Publisher": "213"
	},
	{
		"Title": "\"Last Mughal",
		"Author": " The\"",
		"Genre": "\"Dalrymple",
		"SubGenre": " William\"",
		"Height": "nonfiction",
		"Publisher": "history"
	},
	{
		"Title": "\"Social Choice & Welfare",
		"Author": " Vol 39 No. 1\"",
		"Genre": "Various",
		"SubGenre": "tech",
		"Height": "economics",
		"Publisher": "235"
	},
	{
		"Title": "Radiowaril Bhashane & Shrutika",
		"Author": "\"Deshpande",
		"Genre": " P L\"",
		"SubGenre": "nonfiction",
		"Height": "misc",
		"Publisher": "213"
	},
	{
		"Title": "Gun Gayin Awadi",
		"Author": "\"Deshpande",
		"Genre": " P L\"",
		"SubGenre": "nonfiction",
		"Height": "misc",
		"Publisher": "212"
	},
	{
		"Title": "Aghal Paghal",
		"Author": "\"Deshpande",
		"Genre": " P L\"",
		"SubGenre": "nonfiction",
		"Height": "misc",
		"Publisher": "212"
	},
	{
		"Title": "Maqta-e-Ghalib",
		"Author": "\"Garg",
		"Genre": " Sanjay\"",
		"SubGenre": "nonfiction",
		"Height": "poetry",
		"Publisher": "221"
	},
	{
		"Title": "Beyond Degrees",
		"Author": "",
		"Genre": "philosophy",
		"SubGenre": "education",
		"Height": "222",
		"Publisher": "HarperCollins"
	},
	{
		"Title": "Manasa",
		"Author": "\"Kale",
		"Genre": " V P\"",
		"SubGenre": "nonfiction",
		"Height": "misc",
		"Publisher": "213"
	},
	{
		"Title": "India from Midnight to Milennium",
		"Author": "\"Tharoor",
		"Genre": " Shashi\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "198"
	},
	{
		"Title": "\"World's Greatest Trials",
		"Author": " The\"",
		"Genre": "",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "210"
	},
	{
		"Title": "\"Great Indian Novel",
		"Author": " The\"",
		"Genre": "\"Tharoor",
		"SubGenre": " Shashi\"",
		"Height": "fiction",
		"Publisher": "novel"
	},
	{
		"Title": "O Jerusalem!",
		"Author": "\"Lapierre",
		"Genre": " Dominique\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "217"
	},
	{
		"Title": "\"City of Joy",
		"Author": " The\"",
		"Genre": "\"Lapierre",
		"SubGenre": " Dominique\"",
		"Height": "fiction",
		"Publisher": "novel"
	},
	{
		"Title": "Freedom at Midnight",
		"Author": "\"Lapierre",
		"Genre": " Dominique\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "167"
	},
	{
		"Title": "\"Winter of Our Discontent",
		"Author": " The\"",
		"Genre": "\"Steinbeck",
		"SubGenre": " John\"",
		"Height": "fiction",
		"Publisher": "classic"
	},
	{
		"Title": "On Education",
		"Author": "\"Russell",
		"Genre": " Bertrand\"",
		"SubGenre": "philosophy",
		"Height": "education",
		"Publisher": "203"
	},
	{
		"Title": "Free Will",
		"Author": "\"Harris",
		"Genre": " Sam\"",
		"SubGenre": "nonfiction",
		"Height": "psychology",
		"Publisher": "203"
	},
	{
		"Title": "Bookless in Baghdad",
		"Author": "\"Tharoor",
		"Genre": " Shashi\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "206"
	},
	{
		"Title": "\"Case of the Lame Canary",
		"Author": " The\"",
		"Genre": "\"Gardner",
		"SubGenre": " Earle Stanley\"",
		"Height": "fiction",
		"Publisher": "novel"
	},
	{
		"Title": "\"Theory of Everything",
		"Author": " The\"",
		"Genre": "\"Hawking",
		"SubGenre": " Stephen\"",
		"Height": "science",
		"Publisher": "physics"
	},
	{
		"Title": "New Markets & Other Essays",
		"Author": "\"Drucker",
		"Genre": " Peter\"",
		"SubGenre": "science",
		"Height": "economics",
		"Publisher": "176"
	},
	{
		"Title": "Electric Universe",
		"Author": "\"Bodanis",
		"Genre": " David\"",
		"SubGenre": "science",
		"Height": "physics",
		"Publisher": "201"
	},
	{
		"Title": "\"Hunchback of Notre Dame",
		"Author": " The\"",
		"Genre": "\"Hugo",
		"SubGenre": " Victor\"",
		"Height": "fiction",
		"Publisher": "classic"
	},
	{
		"Title": "Burning Bright",
		"Author": "\"Steinbeck",
		"Genre": " John\"",
		"SubGenre": "fiction",
		"Height": "classic",
		"Publisher": "175"
	},
	{
		"Title": "\"Age of Discontuinity",
		"Author": " The\"",
		"Genre": "\"Drucker",
		"SubGenre": " Peter\"",
		"Height": "nonfiction",
		"Publisher": "economics"
	},
	{
		"Title": "Doctor in the Nude",
		"Author": "\"Gordon",
		"Genre": " Richard\"",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "179"
	},
	{
		"Title": "Down and Out in Paris & London",
		"Author": "\"Orwell",
		"Genre": " George\"",
		"SubGenre": "nonfiction",
		"Height": "autobiography",
		"Publisher": "179"
	},
	{
		"Title": "Identity & Violence",
		"Author": "\"Sen",
		"Genre": " Amartya\"",
		"SubGenre": "philosophy",
		"Height": "philosophy",
		"Publisher": "219"
	},
	{
		"Title": "Beyond the Three Seas",
		"Author": "\"Dalrymple",
		"Genre": " William\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "197"
	},
	{
		"Title": "\"World's Greatest Short Stories",
		"Author": " The\"",
		"Genre": "",
		"SubGenre": "fiction",
		"Height": "classic",
		"Publisher": "217"
	},
	{
		"Title": "Talking Straight",
		"Author": "\"Iacoca",
		"Genre": " Lee\"",
		"SubGenre": "nonfiction",
		"Height": "autobiography",
		"Publisher": "175"
	},
	{
		"Title": "\"Maugham's Collected Short Stories",
		"Author": " Vol 3\"",
		"Genre": "\"Maugham",
		"SubGenre": " William S\"",
		"Height": "fiction",
		"Publisher": "classic"
	},
	{
		"Title": "\"Phantom of Manhattan",
		"Author": " The\"",
		"Genre": "\"Forsyth",
		"SubGenre": " Frederick\"",
		"Height": "fiction",
		"Publisher": "classic"
	},
	{
		"Title": "Ashenden of The British Agent",
		"Author": "\"Maugham",
		"Genre": " William S\"",
		"SubGenre": "fiction",
		"Height": "classic",
		"Publisher": "160"
	},
	{
		"Title": "Zen & The Art of Motorcycle Maintenance",
		"Author": "\"Pirsig",
		"Genre": " Robert\"",
		"SubGenre": "philosophy",
		"Height": "autobiography",
		"Publisher": "172"
	},
	{
		"Title": "\"Great War for Civilization",
		"Author": " The\"",
		"Genre": "\"Fisk",
		"SubGenre": " Robert\"",
		"Height": "nonfiction",
		"Publisher": "history"
	},
	{
		"Title": "We the Living",
		"Author": "\"Rand",
		"Genre": " Ayn\"",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "178"
	},
	{
		"Title": "\"Artist and the Mathematician",
		"Author": " The\"",
		"Genre": "\"Aczel",
		"SubGenre": " Amir\"",
		"Height": "science",
		"Publisher": "mathematics"
	},
	{
		"Title": "History of Western Philosophy",
		"Author": "\"Russell",
		"Genre": " Bertrand\"",
		"SubGenre": "philosophy",
		"Height": "philosophy",
		"Publisher": "213"
	},
	{
		"Title": "Selected Short Stories",
		"Author": "",
		"Genre": "fiction",
		"SubGenre": "classic",
		"Height": "215",
		"Publisher": "Jaico"
	},
	{
		"Title": "Rationality & Freedom",
		"Author": "\"Sen",
		"Genre": " Amartya\"",
		"SubGenre": "science",
		"Height": "economics",
		"Publisher": "213"
	},
	{
		"Title": "Clash of Civilizations and Remaking of the World Order",
		"Author": "\"Huntington",
		"Genre": " Samuel\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "228"
	},
	{
		"Title": "Uncommon Wisdom",
		"Author": "\"Capra",
		"Genre": " Fritjof\"",
		"SubGenre": "nonfiction",
		"Height": "anthology",
		"Publisher": "197"
	},
	{
		"Title": "One",
		"Author": "\"Bach",
		"Genre": " Richard\"",
		"SubGenre": "nonfiction",
		"Height": "autobiography",
		"Publisher": "172"
	},
	{
		"Title": "Karl Marx Biography",
		"Author": "",
		"Genre": "nonfiction",
		"SubGenre": "autobiography",
		"Height": "162",
		"Publisher": ""
	},
	{
		"Title": "To Sir With Love",
		"Author": "Braithwaite",
		"Genre": "fiction",
		"SubGenre": "classic",
		"Height": "197",
		"Publisher": "Penguin"
	},
	{
		"Title": "Half A Life",
		"Author": "\"Naipaul",
		"Genre": " V S\"",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "196"
	},
	{
		"Title": "\"Discovery of India",
		"Author": " The\"",
		"Genre": "\"Nehru",
		"SubGenre": " Jawaharlal\"",
		"Height": "nonfiction",
		"Publisher": "history"
	},
	{
		"Title": "Apulki",
		"Author": "\"Deshpande",
		"Genre": " P L\"",
		"SubGenre": "nonfiction",
		"Height": "misc",
		"Publisher": "211"
	},
	{
		"Title": "Unpopular Essays",
		"Author": "\"Russell",
		"Genre": " Bertrand\"",
		"SubGenre": "philosophy",
		"Height": "philosophy",
		"Publisher": "198"
	},
	{
		"Title": "\"Deceiver",
		"Author": " The\"",
		"Genre": "\"Forsyth",
		"SubGenre": " Frederick\"",
		"Height": "fiction",
		"Publisher": "novel"
	},
	{
		"Title": "Veil: Secret Wars of the CIA",
		"Author": "\"Woodward",
		"Genre": " Bob\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "171"
	},
	{
		"Title": "Char Shabda",
		"Author": "\"Deshpande",
		"Genre": " P L\"",
		"SubGenre": "nonfiction",
		"Height": "misc",
		"Publisher": "214"
	},
	{
		"Title": "Rosy is My Relative",
		"Author": "\"Durrell",
		"Genre": " Gerald\"",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "176"
	},
	{
		"Title": "\"Moon and Sixpence",
		"Author": " The\"",
		"Genre": "\"Maugham",
		"SubGenre": " William S\"",
		"Height": "fiction",
		"Publisher": "classic"
	},
	{
		"Title": "Political Philosophers",
		"Author": "",
		"Genre": "philosophy",
		"SubGenre": "politics",
		"Height": "162",
		"Publisher": ""
	},
	{
		"Title": "\"Short History of the World",
		"Author": " A\"",
		"Genre": "\"Wells",
		"SubGenre": " H G\"",
		"Height": "nonfiction",
		"Publisher": "history"
	},
	{
		"Title": "\"Trembling of a Leaf",
		"Author": " The\"",
		"Genre": "\"Maugham",
		"SubGenre": " William S\"",
		"Height": "fiction",
		"Publisher": "novel"
	},
	{
		"Title": "Doctor on the Brain",
		"Author": "\"Gordon",
		"Genre": " Richard\"",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "204"
	},
	{
		"Title": "Simpsons & Their Mathematical Secrets",
		"Author": "\"Singh",
		"Genre": " Simon\"",
		"SubGenre": "science",
		"Height": "mathematics",
		"Publisher": "233"
	},
	{
		"Title": "Pattern Classification",
		"Author": "\"Duda",
		"Genre": " Hart\"",
		"SubGenre": "tech",
		"Height": "data_science",
		"Publisher": "241"
	},
	{
		"Title": "From Beirut to Jerusalem",
		"Author": "\"Friedman",
		"Genre": " Thomas\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "202"
	},
	{
		"Title": "\"Code Book",
		"Author": " The\"",
		"Genre": "\"Singh",
		"SubGenre": " Simon\"",
		"Height": "science",
		"Publisher": "mathematics"
	},
	{
		"Title": "\"Age of the Warrior",
		"Author": " The\"",
		"Genre": "\"Fisk",
		"SubGenre": " Robert\"",
		"Height": "nonfiction",
		"Publisher": "history"
	},
	{
		"Title": "Final Crisis",
		"Author": "",
		"Genre": "fiction",
		"SubGenre": "comic",
		"Height": "257",
		"Publisher": ""
	},
	{
		"Title": "\"Killing Joke",
		"Author": " The\"",
		"Genre": "",
		"SubGenre": "fiction",
		"Height": "comic",
		"Publisher": "283"
	},
	{
		"Title": "Flashpoint",
		"Author": "",
		"Genre": "fiction",
		"SubGenre": "comic",
		"Height": "265",
		"Publisher": ""
	},
	{
		"Title": "Batman Earth One",
		"Author": "",
		"Genre": "fiction",
		"SubGenre": "comic",
		"Height": "265",
		"Publisher": ""
	},
	{
		"Title": "Crisis on Infinite Earths",
		"Author": "",
		"Genre": "fiction",
		"SubGenre": "comic",
		"Height": "258",
		"Publisher": ""
	},
	{
		"Title": "\"Numbers Behind Numb3rs",
		"Author": " The\"",
		"Genre": "\"Devlin",
		"SubGenre": " Keith\"",
		"Height": "science",
		"Publisher": "mathematics"
	},
	{
		"Title": "Superman Earth One - 1",
		"Author": "",
		"Genre": "fiction",
		"SubGenre": "comic",
		"Height": "259",
		"Publisher": ""
	},
	{
		"Title": "Superman Earth One - 2",
		"Author": "",
		"Genre": "fiction",
		"SubGenre": "comic",
		"Height": "258",
		"Publisher": ""
	},
	{
		"Title": "Justice League: Throne of Atlantis",
		"Author": "",
		"Genre": "fiction",
		"SubGenre": "comic",
		"Height": "258",
		"Publisher": ""
	},
	{
		"Title": "Justice League: The Villain's Journey",
		"Author": "",
		"Genre": "fiction",
		"SubGenre": "comic",
		"Height": "258",
		"Publisher": ""
	},
	{
		"Title": "\"Death of Superman",
		"Author": " The\"",
		"Genre": "",
		"SubGenre": "fiction",
		"Height": "comic",
		"Publisher": "258"
	},
	{
		"Title": "History of the DC Universe",
		"Author": "",
		"Genre": "fiction",
		"SubGenre": "comic",
		"Height": "258",
		"Publisher": ""
	},
	{
		"Title": "Batman: The Long Halloween",
		"Author": "",
		"Genre": "fiction",
		"SubGenre": "comic",
		"Height": "258",
		"Publisher": ""
	},
	{
		"Title": "\"Life in Letters",
		"Author": " A\"",
		"Genre": "\"Steinbeck",
		"SubGenre": " John\"",
		"Height": "nonfiction",
		"Publisher": "autobiography"
	},
	{
		"Title": "\"Information",
		"Author": " The\"",
		"Genre": "\"Gleick",
		"SubGenre": " James\"",
		"Height": "science",
		"Publisher": "mathematics"
	},
	{
		"Title": "\"Journal of Economics",
		"Author": " vol 106 No 3\"",
		"Genre": "",
		"SubGenre": "science",
		"Height": "economics",
		"Publisher": "235"
	},
	{
		"Title": "Elements of Information Theory",
		"Author": "\"Thomas",
		"Genre": " Joy\"",
		"SubGenre": "tech",
		"Height": "signal_processing",
		"Publisher": "229"
	},
	{
		"Title": "Power Electronics - Rashid",
		"Author": "\"Rashid",
		"Genre": " Muhammad\"",
		"SubGenre": "tech",
		"Height": "computer_science",
		"Publisher": "235"
	},
	{
		"Title": "Power Electronics - Mohan",
		"Author": "\"Mohan",
		"Genre": " Ned\"",
		"SubGenre": "tech",
		"Height": "computer_science",
		"Publisher": "237"
	},
	{
		"Title": "Neural Networks",
		"Author": "\"Haykin",
		"Genre": " Simon\"",
		"SubGenre": "tech",
		"Height": "data_science",
		"Publisher": "240"
	},
	{
		"Title": "\"Grapes of Wrath",
		"Author": " The\"",
		"Genre": "\"Steinbeck",
		"SubGenre": " John\"",
		"Height": "fiction",
		"Publisher": "classic"
	},
	{
		"Title": "Vyakti ani Valli",
		"Author": "\"Deshpande",
		"Genre": " P L\"",
		"SubGenre": "nonfiction",
		"Height": "misc",
		"Publisher": "211"
	},
	{
		"Title": "Statistical Learning Theory",
		"Author": "\"Vapnik",
		"Genre": " Vladimir\"",
		"SubGenre": "tech",
		"Height": "data_science",
		"Publisher": "228"
	},
	{
		"Title": "Empire of the Mughal - The Tainted Throne",
		"Author": "\"Rutherford",
		"Genre": " Alex\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "180"
	},
	{
		"Title": "Empire of the Mughal - Brothers at War",
		"Author": "\"Rutherford",
		"Genre": " Alex\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "180"
	},
	{
		"Title": "Empire of the Mughal - Ruler of the World",
		"Author": "\"Rutherford",
		"Genre": " Alex\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "180"
	},
	{
		"Title": "Empire of the Mughal - The Serpent's Tooth",
		"Author": "\"Rutherford",
		"Genre": " Alex\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "180"
	},
	{
		"Title": "Empire of the Mughal - Raiders from the North",
		"Author": "\"Rutherford",
		"Genre": " Alex\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "180"
	},
	{
		"Title": "Mossad",
		"Author": "\"Baz-Zohar",
		"Genre": " Michael\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "236"
	},
	{
		"Title": "Jim Corbett Omnibus",
		"Author": "\"Corbett",
		"Genre": " Jim\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "223"
	},
	{
		"Title": "20000 Leagues Under the Sea",
		"Author": "\"Verne",
		"Genre": " Jules\"",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "190"
	},
	{
		"Title": "Batatyachi Chal",
		"Author": "Deshpande P L",
		"Genre": "fiction",
		"SubGenre": "novel",
		"Height": "200",
		"Publisher": ""
	},
	{
		"Title": "Hafasavnuk",
		"Author": "Deshpande P L",
		"Genre": "fiction",
		"SubGenre": "novel",
		"Height": "211",
		"Publisher": ""
	},
	{
		"Title": "Urlasurla",
		"Author": "Deshpande P L",
		"Genre": "fiction",
		"SubGenre": "novel",
		"Height": "211",
		"Publisher": ""
	},
	{
		"Title": "Pointers in C",
		"Author": "\"Kanetkar",
		"Genre": " Yashwant\"",
		"SubGenre": "tech",
		"Height": "computer_science",
		"Publisher": "213"
	},
	{
		"Title": "\"Cathedral and the Bazaar",
		"Author": " The\"",
		"Genre": "\"Raymond",
		"SubGenre": " Eric\"",
		"Height": "tech",
		"Publisher": "computer_science"
	},
	{
		"Title": "Design with OpAmps",
		"Author": "\"Franco",
		"Genre": " Sergio\"",
		"SubGenre": "tech",
		"Height": "computer_science",
		"Publisher": "240"
	},
	{
		"Title": "Think Complexity",
		"Author": "\"Downey",
		"Genre": " Allen\"",
		"SubGenre": "tech",
		"Height": "data_science",
		"Publisher": "230"
	},
	{
		"Title": "\"Devil's Advocate",
		"Author": " The\"",
		"Genre": "\"West",
		"SubGenre": " Morris\"",
		"Height": "fiction",
		"Publisher": "novel"
	},
	{
		"Title": "Ayn Rand Answers",
		"Author": "\"Rand",
		"Genre": " Ayn\"",
		"SubGenre": "philosophy",
		"Height": "objectivism",
		"Publisher": "203"
	},
	{
		"Title": "Philosophy: Who Needs It",
		"Author": "\"Rand",
		"Genre": " Ayn\"",
		"SubGenre": "philosophy",
		"Height": "objectivism",
		"Publisher": "171"
	},
	{
		"Title": "\"World's Great Thinkers",
		"Author": " The\"",
		"Genre": "",
		"SubGenre": "science",
		"Height": "physics",
		"Publisher": "189"
	},
	{
		"Title": "Data Analysis with Open Source Tools",
		"Author": "\"Janert",
		"Genre": " Phillip\"",
		"SubGenre": "tech",
		"Height": "data_science",
		"Publisher": "230"
	},
	{
		"Title": "Broca's Brain",
		"Author": "\"Sagan",
		"Genre": " Carl\"",
		"SubGenre": "science",
		"Height": "physics",
		"Publisher": "174"
	},
	{
		"Title": "Men of Mathematics",
		"Author": "\"Bell",
		"Genre": " E T\"",
		"SubGenre": "science",
		"Height": "mathematics",
		"Publisher": "217"
	},
	{
		"Title": "Oxford book of Modern Science Writing",
		"Author": "\"Dawkins",
		"Genre": " Richard\"",
		"SubGenre": "science",
		"Height": "science",
		"Publisher": "240"
	},
	{
		"Title": "\"Justice",
		"Author": " Judiciary and Democracy\"",
		"Genre": "\"Ranjan",
		"SubGenre": " Sudhanshu\"",
		"Height": "nonfiction",
		"Publisher": "legal"
	},
	{
		"Title": "\"Arthashastra",
		"Author": " The\"",
		"Genre": "Kautiyla",
		"SubGenre": "philosophy",
		"Height": "philosophy",
		"Publisher": "214"
	},
	{
		"Title": "We the People",
		"Author": "Palkhivala",
		"Genre": "philosophy",
		"SubGenre": "philosophy",
		"Height": "216",
		"Publisher": ""
	},
	{
		"Title": "We the Nation",
		"Author": "Palkhivala",
		"Genre": "philosophy",
		"SubGenre": "philosophy",
		"Height": "216",
		"Publisher": ""
	},
	{
		"Title": "\"Courtroom Genius",
		"Author": " The\"",
		"Genre": "Sorabjee",
		"SubGenre": "nonfiction",
		"Height": "autobiography",
		"Publisher": "217"
	},
	{
		"Title": "Dongri to Dubai",
		"Author": "\"Zaidi",
		"Genre": " Hussain\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "216"
	},
	{
		"Title": "\"History of England",
		"Author": " Foundation\"",
		"Genre": "\"Ackroyd",
		"SubGenre": " Peter\"",
		"Height": "nonfiction",
		"Publisher": "history"
	},
	{
		"Title": "City of Djinns",
		"Author": "\"Dalrymple",
		"Genre": " William\"",
		"SubGenre": "nonfiction",
		"Height": "history",
		"Publisher": "198"
	},
	{
		"Title": "India's Legal System",
		"Author": "Nariman",
		"Genre": "nonfiction",
		"SubGenre": "legal",
		"Height": "177",
		"Publisher": ""
	},
	{
		"Title": "More Tears to Cry",
		"Author": "\"Sassoon",
		"Genre": " Jean\"",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "235"
	},
	{
		"Title": "\"Ropemaker",
		"Author": " The\"",
		"Genre": "\"Dickinson",
		"SubGenre": " Peter\"",
		"Height": "fiction",
		"Publisher": "novel"
	},
	{
		"Title": "Angels & Demons",
		"Author": "\"Brown",
		"Genre": " Dan\"",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "170"
	},
	{
		"Title": "\"Judge",
		"Author": " The\"",
		"Genre": "",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "170"
	},
	{
		"Title": "\"Attorney",
		"Author": " The\"",
		"Genre": "",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "170"
	},
	{
		"Title": "\"Prince",
		"Author": " The\"",
		"Genre": "Machiavelli",
		"SubGenre": "fiction",
		"Height": "classic",
		"Publisher": "173"
	},
	{
		"Title": "Eyeless in Gaza",
		"Author": "\"Huxley",
		"Genre": " Aldous\"",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "180"
	},
	{
		"Title": "Tales of Beedle the Bard",
		"Author": "\"Rowling",
		"Genre": " J K\"",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "184"
	},
	{
		"Title": "Girl with the Dragon Tattoo",
		"Author": "\"Larsson",
		"Genre": " Steig\"",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "179"
	},
	{
		"Title": "Girl who kicked the Hornet's Nest",
		"Author": "\"Larsson",
		"Genre": " Steig\"",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "179"
	},
	{
		"Title": "Girl who played with Fire",
		"Author": "\"Larsson",
		"Genre": " Steig\"",
		"SubGenre": "fiction",
		"Height": "novel",
		"Publisher": "179"
	},
	{
		"Title": "Batman Handbook",
		"Author": "",
		"Genre": "fiction",
		"SubGenre": "comic",
		"Height": "270",
		"Publisher": ""
	},
	{
		"Title": "Murphy's Law",
		"Author": "",
		"Genre": "philosophy",
		"SubGenre": "psychology",
		"Height": "178",
		"Publisher": ""
	},
	{
		"Title": "Structure and Randomness",
		"Author": "\"Tao",
		"Genre": " Terence\"",
		"SubGenre": "science",
		"Height": "mathematics",
		"Publisher": "252"
	},
	{
		"Title": "Image Processing with MATLAB",
		"Author": "\"Eddins",
		"Genre": " Steve\"",
		"SubGenre": "tech",
		"Height": "signal_processing",
		"Publisher": "241"
	},
	{
		"Title": "Animal Farm",
		"Author": "\"Orwell",
		"Genre": " George\"",
		"SubGenre": "fiction",
		"Height": "classic",
		"Publisher": "180"
	},
	{
		"Title": "\"Idiot",
		"Author": " The\"",
		"Genre": "\"Dostoevsky",
		"SubGenre": " Fyodor\"",
		"Height": "fiction",
		"Publisher": "classic"
	},
	{
		"Title": "\"Christmas Carol",
		"Author": " A\"",
		"Genre": "\"Dickens",
		"SubGenre": " Charles\"",
		"Height": "fiction",
		"Publisher": "classic"
	}
]


class NewTree:

    def __init__(self, value, parent=None):
        self.value = value
        self.children = []

        self.parent = parent

    def __getitem__(self, item):
        return item


def set_pandas_options():
	pd.set_option('display.max_rows', None)
	pd.set_option('display.max_columns', None)
	pd.set_option('display.width', 400)




def create_dataframe(link):
	return pd.read_csv(link)



def create_tree(genres, books_grouped):
	root = NewTree("Books")
	for i in range(len(genres)):
		genre_node = NewTree(genres[i], parent=root)
		# Root.children.append((firstNode))
		current_group = books_grouped[i]
		current_subgenre = current_group[1]


		split_subgenres = list(current_subgenre.groupby("SubGenre"))
		for j in range(len(split_subgenres)):

			subgenre_node = NewTree(split_subgenres[j][0], parent=genre_node)

			for k in split_subgenres[j][1:]:

				for row in k.itertuples():

					book_node = NewTree([row[1], row[2], row[3]], parent=subgenre_node)

					subgenre_node.children.append(book_node)

			genre_node.children.append(subgenre_node)

		root.children.append(genre_node)
	return root

if __name__ == "__main__":
	set_pandas_options()
	df = create_dataframe(r'./books_new.csv')
	new_df = df.sort_values(by=['Genre', 'SubGenre'])
	grouped = new_df.groupby(['Genre'])
	list_of_grouped_books = list(grouped)
	genre_information = new_df.Genre.unique()
	current_tree = create_tree(genre_information, list_of_grouped_books)
	print('inhere')








