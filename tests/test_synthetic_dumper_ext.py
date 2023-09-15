from nr_metadata.documents.records.api import DocumentsRecord


def test_synthetic_dumper_extension(app, db, sample_metadata):
    record = DocumentsRecord.create(sample_metadata)
    db.session.commit()

    dump = record.dumps()
    assert "syntheticFields" in dump

    contributors_full_names = [
        contributor["fullName"] for contributor in sample_metadata["contributors"]
    ]
    creators_full_names = [
        creator["fullName"] for creator in sample_metadata["creators"]
    ]
    assert sorted(dump["syntheticFields"]["person"]) == sorted(
        contributors_full_names + creators_full_names
    )

    degree_grantors = sample_metadata["thesis"]["degreeGrantors"]
    degree_grantors.extend(
        [
            contributor
            for contributor in sample_metadata["contributors"]
            if "affiliation" in contributor
        ]
    )
    assert sorted(
        dump["syntheticFields"]["institutions"], key=lambda d: d["id"]
    ) == sorted(degree_grantors, key=lambda d: d["id"])

    all_records_subjects = [
        item for subject in sample_metadata["subjects"] for item in subject["subject"]
    ]
    record_keywords_cs = list(
        map(
            lambda s: s["value"],
            filter(lambda s: s["lang"] == "cs", all_records_subjects),
        )
    )
    record_keywords_en = list(
        map(
            lambda s: s["value"],
            filter(lambda s: s["lang"] == "en", all_records_subjects),
        )
    )
    assert sorted(dump["syntheticFields"]["keywords_cs"]) == sorted(record_keywords_cs)
    assert sorted(dump["syntheticFields"]["keywords_en"]) == sorted(record_keywords_en)

    new_record = DocumentsRecord.loads(dump)
    assert "syntheticFields" not in new_record
