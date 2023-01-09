import pandas as pd
import polyline

# Pandas is the easiest way to approach Tableau's "dictionary of lists" format. Going forward DL stands for "dict of lists" and LD for... the opposite.

input_ld = pd.DataFrame(_arg1).to_dict(orient="records")
output_ld = []

for record in input_ld:
    for i, coordinate_pair in enumerate(polyline.decode(record.get("map_summary_polyline", ""))):
        output_ld.append({
            "id": str(record.get("id", 0)), # We need to treat ID as string, because Tableau gets confused otherwise
            "seq": i,
            "lat": coordinate_pair[0],
            "lon": coordinate_pair[1]
        })

output_dl = pd.DataFrame(output_ld).to_dict(orient="list")
return output_dl