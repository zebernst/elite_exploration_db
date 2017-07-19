def split_sysname(namestr):
	# split system name into sector and system name, also maybe give info about what the name means??
	pass

def solarmasses_to_kg(stellar_mass):
	# convert stellar masses from multiples of the sun's mass to kilograms
	return float(stellar_mass) / (1.989*10**30) 

def megatonnes_to_kg(mass_mt):
	# convert ring mass from (metric?) megatonnes to kilograms
	return float(mass_mt) / float(1000000000) # because python is funky with its integer division
	
