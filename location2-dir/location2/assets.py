from dagster import asset, AssetKey

@asset(key_prefix=["source","netsuite"])
def fx_rates():
    pass

@asset(deps=[AssetKey(["fx_rates"])])
def downstream_asset():
    pass
