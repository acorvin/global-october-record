"""Downloads the raw data for the study into data/raw. No API keys are needed.
    python3 scripts/download_data.py
"""
import json
import urllib.request
from datetime import date
from pathlib import Path

raw = Path(__file__).resolve().parents[1] / "data" / "raw"
raw.mkdir(parents=True, exist_ok=True)

SOURCES = {
    "gistemp_global_monthly.csv": "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv",
    "noaaglobaltemp_october.csv": "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/tavg/land_ocean/1/10/1850-2026/data.csv",
    "era5_daily_global_2t.csv": "https://sites.ecmwf.int/data/climatepulse/data/series/era5_daily_series_2t_global.csv",
    "oni.ascii.txt": "https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt",
    "RONI.ascii.txt": "https://www.cpc.ncep.noaa.gov/data/indices/RONI.ascii.txt",
}
for name, url in SOURCES.items():
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    (raw / name).write_bytes(urllib.request.urlopen(req, timeout=120).read())
    print("saved", name)
(raw / "download.json").write_text(json.dumps({"downloaded": date.today().isoformat(), "sources": SOURCES}, indent=1))
