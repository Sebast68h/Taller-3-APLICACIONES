import pandas as pd
escala = ["ordinal","Nominal","continua","continua","nominal","continua","continua","continua","nominal","ordinal","ordinal","discreto","discreto","ordinal","ordinal","nominal","ordinal","discreto","nominal"]
df = pd.read_csv("estudiantes - copy.csv")
ejemplo = ["E0456","Administración","2","19","Mujer","17.7","5.8","47.0","Caminando","4","4","3","4.9","Frecuentemente","1","IA y ML","Presencial","3.24","2026-08-04"]
dcd = {"variables" : df.columns,
       "tipo_python":df.dtypes,
       "escala": escala,
       "descripcion": 0,
       "ejemplo": ejemplo }

df = pd.DataFrame(dcd)
print(df)