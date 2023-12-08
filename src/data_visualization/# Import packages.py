from datafed.CommandLib import API
df_api = API()
pl_resp = df_api.projectList()
print(pl_resp)
print(type(pl_resp), len(pl_resp))
type(pl_resp[0])
print(df_api.getContext())
print(df_api.collectionView("root", context="p/trn001"))