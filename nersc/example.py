from nbodykit.lab import *
from nbodykit import setup_logging

setup_logging("debug")

cosmo = cosmology.Planck15

Plin = cosmology.EHPower(cosmo, redshift=0.55)
# lognormal particles
source = Source.LogNormal(Plin=Plin, nbar=3e-7, BoxSize=1380., Nmesh=8, seed=42)
                
# apply RSD
source['Position'] += source['VelocityOffset'] * [0,0,1]

# compute P(k,mu) and multipoles
result = FFTPower(source, mode='2d', poles=[0,2,4], los=[0,0,1])

# and save
output = "./test_zeldovich.json"
result.save(output)
