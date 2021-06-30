from functools import reduce

string_to_replace = {
    "asset_class": "assetClass",
    "fs_version": "fsVersion",
    "fs_versionlink_id": "fsVersionLinkId",
    "key_des": "keyDesc",
    "sec_version": "secVersion",
    "sec_versionlink_id": "secVersionLinkId",
    "securityId": "securityId",
    "source_id": "sourceId",
    "sub_sector": "subSector"
}

sample_string = f"The asset_class fs_version fs_versionlink_id key_des " \
            f"sec_version sec_versionlink_id securityId source_id sub_sector completed"

converted_string = reduce(lambda a, kv: a.replace(*kv),
                          string_to_replace.items(), sample_string)

print(sample_string)
print(converted_string)
