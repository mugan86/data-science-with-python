# Básico con pandas

## 1 Cargar datos (CSV)

Qué hace: lee un CSV y crea un `DataFrame`.

```python
import pandas as pd
from project.config import get_file_path, FileExtension, Project

filePath = get_file_path("shots", FileExtension.CSV, Project.BASKETBALL)
shots = pd.read_csv(filePath)
```

Atajos útiles (opciones comunes):

```python
# parsear fechas, seleccionar columnas y controlar tipos
shots = pd.read_csv(filePath,
                    parse_dates=['date'],        # convertir columnas fecha
                    usecols=['shot_id','name','dist','value','made','period'],
                    dtype={'shot_id': int},      # fuerza tipos
                    nrows=10000,                 # solo las primeras n filas (útil para dev)
                    low_memory=False)            # evitar warnings de tipos mixtos
```

### Errores comunes

- No pasar `parse_dates` si esperas trabajar con tiempos (luego tocará convertir manualmente).

- Archivos grandes → usar `chunksize` o `nrows` para pruebas.

## 2 Inspección inicial

`Objetivo`: entender tamaño, columnas y tipos.

```python
print(type(shots))         # <class 'pandas.core.frame.DataFrame'>
print(shots.head())        # primeros 5 registros
print(shots.columns)       # nombres de columnas
print(shots.shape)         # (n_rows, n_columns)
print(shots.info())        # dtypes, non-null counts
print(shots.describe())    # resumen estadístico para columnas numéricas
print(shots.sample(5))     # 5 filas al azar
```

**Consejo práctico**: usa `shots.info()` antes de hacer `astype` o imputaciones para ver valores nulos y tipos.

Errores comunes

Leer CSV con delimitador distinto (uso `sep=';'` si corresponde).

Con `low_memory=True` pandas puede inferir tipos de columna de manera inconsistente → usar `low_memory=False`.

## 3 Subconjuntos de columnas (Series vs DataFrame)

- **Single bracket** → Series
- **Double bracket** → DataFrame

```python
# Series (una columna)
s = shots['name']              # type: pandas.Series
s.head()

# DataFrame (una columna pero como df)
df_one = shots['name'].to_frame()

# Varias columnas -> DataFrame
df = shots[['name', 'dist', 'value', 'made']]  # type: pandas.DataFrame

# Nota: esto lanza error
# shots['name', 'dist', 'value', 'made']   # ❌ forma incorrecta
```

### Uso típico

- `shots['col']` para operaciones vectorizadas y series (ej. .`value_counts()`).

- `shots[['a','b']]` para pasar a funciones que esperan DataFrame.

### Peculiaridades

- `df.column` (atributo) funciona sólo si el nombre es un identificador válido y no colisiona con métodos; es preferible `df['column']`.

- `df[['col']].head()` devuelve DataFrame; su `.type es` distinto al de `df['col']`.

### Errores comunes

Confundir `Series` y `DataFrame` (por ejemplo al usar `.merge()` o `.to_csv()` con columnas).

## 4 Indexación (set_index, reset_index, .loc, .iloc)

### Set / reset index

```python
# ver un ejemplo rápido (sin modificar original)
print(shots.set_index('shot_id').head())

# modificar en sitio
shots.set_index('shot_id', inplace=True)
# o (preferible por claridad):
shots = shots.set_index('shot_id')

# volver al index numérico por defecto
shots = shots.reset_index()
```

### .loc (label-based) y .iloc (position-based)

```python
# Filtrar filas por condición y seleccionar columnas (label-based)
shots_ot = shots.loc[shots['period'] > 4, ['name', 'dist', 'value']]

# Selección por posición
first_three_rows = shots.iloc[0:3, 0:4]  # filas 0-2, columnas 0-3

# Ejemplo de ordenación
shots_ot = shots_ot.sort_values('name')   # devuelve nuevo DF
# o inplace:
shots_ot.sort_values('name', inplace=True)
```

### Asignación y alineamiento por index

```python
# si shots_ot y shots comparten índices, la asignación se alinea por índice
shots_ot['made'] = shots['made']   # los valores se alinean por index
```

| Acción                   | Código                                   |
| ------------------------ | ---------------------------------------- |
| Leer CSV                 | `pd.read_csv("file.csv")`                |
| Ver primeras filas       | `df.head(5)`                             |
| Nombres de columnas      | `df.columns`                             |
| Tamaño (filas, columnas) | `df.shape`                               |
| Resumen tipos / nulos    | `df.info()`                              |
| Estadísticas básicas     | `df.describe()`                          |
| Seleccionar columna      | `df['col']`                              |
| Seleccionar varias       | `df[['col1','col2']]`                    |
| Filtrar filas            | `df.loc[df['col'] > 10]`                 |
| Filtrar filas + columnas | `df.loc[df['col'] > 10, ['a','b']]`      |
| Selección por posición   | `df.iloc[0:5, 0:3]`                      |
| Cambiar índice           | `df.set_index('col')`                    |
| Resetear índice          | `df.reset_index()`                       |
| Ordenar                  | `df.sort_values('col', ascending=False)` |
| Nueva columna            | `df['new'] = df['a'] + df['b']`          |
| Exportar CSV             | `df.to_csv("out.csv", index=False)`      |
