on_api =['file1', 'file2', 'file3']
alternative_keys = {'file1':['plan_id', 'node_id'],
                    'file2':['plan_id', 'node_id']}
gem_api = []
instance = "prod"
all_files = on_api + gem_api
settings = dict(onApi=on_api,
                gemApi=gem_api,
                files_to_db_update=all_files,
                instance_type=instance)

