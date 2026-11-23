# Appeal path and bad-input log check — before

- Produced by: `run_appeals.py::run_trial`
- Service: `app.py::appeal`, `app.py::submit`
- 3 trials · 2026-11-22 22:10

## Trial 1

```json
{
  "appeals": [
    {
      "content_id": "08c87851-d516-4b76-9c63-dc4cb540880e",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "08c87851-d516-4b76-9c63-dc4cb540880e",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "45d15d89-8522-404d-8f86-2fd34c1003b9",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "45d15d89-8522-404d-8f86-2fd34c1003b9",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "d9e4a410-8629-46b2-a541-04156f47dcce",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "d9e4a410-8629-46b2-a541-04156f47dcce",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "54f9b6a0-4533-4e7b-93f6-19d8e8b6e375",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "54f9b6a0-4533-4e7b-93f6-19d8e8b6e375",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "e91ecd05-1d1e-4bf7-a2ec-fe0a1adbd23e",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "e91ecd05-1d1e-4bf7-a2ec-fe0a1adbd23e",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "43720ff9-efcf-4f4c-b584-e16ac785e343",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "43720ff9-efcf-4f4c-b584-e16ac785e343",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "573fa433-ec24-49c5-b400-6c200c10d2b8",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "573fa433-ec24-49c5-b400-6c200c10d2b8",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "8884ab04-00b8-44e1-a428-39ebff5323f1",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "8884ab04-00b8-44e1-a428-39ebff5323f1",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "345da8d8-db21-48ed-be30-c6d550dae45f",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "345da8d8-db21-48ed-be30-c6d550dae45f",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "341791f6-1b01-4dea-a949-5978880ba045",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "341791f6-1b01-4dea-a949-5978880ba045",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    }
  ],
  "made_up_id": {
    "status": 404,
    "response": {
      "error": "unknown_content_id",
      "message": "We couldn't find a submission with that content_id."
    },
    "log_entries_added": 0,
    "passed": true
  },
  "bad_input_log_check": [
    {
      "sent": {
        "creator_id": "eval_bad_missing_appeals_t1"
      },
      "status": 400,
      "response": {
        "error": "missing_text",
        "message": "text is required."
      },
      "new_log_entries": [
        {
          "event": "rejected",
          "status": "rejected",
          "reason": "missing_text"
        }
      ],
      "passed": true
    },
    {
      "sent": {
        "text": null,
        "creator_id": "eval_bad_null_appeals_t1"
      },
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a string."
      },
      "new_log_entries": [
        {
          "event": "rejected",
          "status": "rejected",
          "reason": "invalid_text"
        }
      ],
      "passed": true
    },
    {
      "sent": {
        "text": "",
        "creator_id": "eval_bad_empty_appeals_t1"
      },
      "status": 400,
      "response": {
        "error": "empty_text",
        "message": "text is empty."
      },
      "new_log_entries": [
        {
          "event": "rejected",
          "status": "rejected",
          "reason": "empty_text"
        }
      ],
      "passed": true
    },
    {
      "sent": {
        "text": "   \t  ",
        "creator_id": "eval_bad_whitespace_appeals_t1"
      },
      "status": 400,
      "response": {
        "error": "empty_text",
        "message": "text is empty."
      },
      "new_log_entries": [
        {
          "event": "rejected",
          "status": "rejected",
          "reason": "empty_text"
        }
      ],
      "passed": true
    },
    {
      "sent": {
        "text": "<10005 chars>",
        "creator_id": "eval_bad_huge_appeals_t1"
      },
      "status": 400,
      "response": {
        "error": "text_too_long",
        "message": "text is longer than 10,000 characters."
      },
      "new_log_entries": [
        {
          "event": "rejected",
          "status": "rejected",
          "reason": "text_too_long"
        }
      ],
      "passed": true
    }
  ]
}
```

## Trial 2

```json
{
  "appeals": [
    {
      "content_id": "f1c354da-d0eb-413a-a2e4-e0cb6cc67e8d",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "f1c354da-d0eb-413a-a2e4-e0cb6cc67e8d",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "2b60ec69-128a-49d6-98ea-1382706c7324",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "2b60ec69-128a-49d6-98ea-1382706c7324",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "87c54fe2-2139-4ae9-8a68-64ea38d0367c",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "87c54fe2-2139-4ae9-8a68-64ea38d0367c",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "5722fb1f-382e-48c2-add6-211e7bab812b",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "5722fb1f-382e-48c2-add6-211e7bab812b",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "b752d890-a77f-465b-b58d-5b9ec8fe0059",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "b752d890-a77f-465b-b58d-5b9ec8fe0059",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "5e4f3a63-581d-475e-9531-9104b4b48689",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "5e4f3a63-581d-475e-9531-9104b4b48689",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "9f0ae6f6-0711-43b6-b525-7fcd0f2e32f9",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "9f0ae6f6-0711-43b6-b525-7fcd0f2e32f9",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "cea050c1-1eb9-490c-b084-4f743400deb6",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "cea050c1-1eb9-490c-b084-4f743400deb6",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "d971fff2-0ab9-4ac4-9dbe-c79b226dab5e",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "d971fff2-0ab9-4ac4-9dbe-c79b226dab5e",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "bd56b4f8-ac68-4f03-8aa2-4b314359306b",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "bd56b4f8-ac68-4f03-8aa2-4b314359306b",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    }
  ],
  "made_up_id": {
    "status": 404,
    "response": {
      "error": "unknown_content_id",
      "message": "We couldn't find a submission with that content_id."
    },
    "log_entries_added": 0,
    "passed": true
  },
  "bad_input_log_check": [
    {
      "sent": {
        "creator_id": "eval_bad_missing_appeals_t2"
      },
      "status": 400,
      "response": {
        "error": "missing_text",
        "message": "text is required."
      },
      "new_log_entries": [
        {
          "event": "rejected",
          "status": "rejected",
          "reason": "missing_text"
        }
      ],
      "passed": true
    },
    {
      "sent": {
        "text": null,
        "creator_id": "eval_bad_null_appeals_t2"
      },
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a string."
      },
      "new_log_entries": [
        {
          "event": "rejected",
          "status": "rejected",
          "reason": "invalid_text"
        }
      ],
      "passed": true
    },
    {
      "sent": {
        "text": "",
        "creator_id": "eval_bad_empty_appeals_t2"
      },
      "status": 400,
      "response": {
        "error": "empty_text",
        "message": "text is empty."
      },
      "new_log_entries": [
        {
          "event": "rejected",
          "status": "rejected",
          "reason": "empty_text"
        }
      ],
      "passed": true
    },
    {
      "sent": {
        "text": "   \t  ",
        "creator_id": "eval_bad_whitespace_appeals_t2"
      },
      "status": 400,
      "response": {
        "error": "empty_text",
        "message": "text is empty."
      },
      "new_log_entries": [
        {
          "event": "rejected",
          "status": "rejected",
          "reason": "empty_text"
        }
      ],
      "passed": true
    },
    {
      "sent": {
        "text": "<10005 chars>",
        "creator_id": "eval_bad_huge_appeals_t2"
      },
      "status": 400,
      "response": {
        "error": "text_too_long",
        "message": "text is longer than 10,000 characters."
      },
      "new_log_entries": [
        {
          "event": "rejected",
          "status": "rejected",
          "reason": "text_too_long"
        }
      ],
      "passed": true
    }
  ]
}
```

## Trial 3

```json
{
  "appeals": [
    {
      "content_id": "2dd297f4-d2ce-4cdf-97b5-ef6be0207534",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "2dd297f4-d2ce-4cdf-97b5-ef6be0207534",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "9e05f11b-07d3-497c-9251-efb83347cd67",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "9e05f11b-07d3-497c-9251-efb83347cd67",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "1a6a9d39-0055-489a-9d72-21b60e4bb4b3",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "1a6a9d39-0055-489a-9d72-21b60e4bb4b3",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "0c05c424-27d6-4897-84cb-f6833b25de90",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "0c05c424-27d6-4897-84cb-f6833b25de90",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "6bbbe8a0-95d5-4a01-9fa2-d5f0a227ad26",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "6bbbe8a0-95d5-4a01-9fa2-d5f0a227ad26",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "cf45408d-4b12-4200-a787-e811db7546c2",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "cf45408d-4b12-4200-a787-e811db7546c2",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "c49b1d6b-c111-41df-b2e0-511ef34c0962",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "c49b1d6b-c111-41df-b2e0-511ef34c0962",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "9d7e994c-5753-4a0d-a1a6-bd9e0a1557dc",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "9d7e994c-5753-4a0d-a1a6-bd9e0a1557dc",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "db96b6c6-37ed-47e7-a8a9-d79eb467c443",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "db96b6c6-37ed-47e7-a8a9-d79eb467c443",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "79a07ad2-2313-497f-9b83-3f5a0574d10b",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "79a07ad2-2313-497f-9b83-3f5a0574d10b",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    }
  ],
  "made_up_id": {
    "status": 404,
    "response": {
      "error": "unknown_content_id",
      "message": "We couldn't find a submission with that content_id."
    },
    "log_entries_added": 0,
    "passed": true
  },
  "bad_input_log_check": [
    {
      "sent": {
        "creator_id": "eval_bad_missing_appeals_t3"
      },
      "status": 400,
      "response": {
        "error": "missing_text",
        "message": "text is required."
      },
      "new_log_entries": [
        {
          "event": "rejected",
          "status": "rejected",
          "reason": "missing_text"
        }
      ],
      "passed": true
    },
    {
      "sent": {
        "text": null,
        "creator_id": "eval_bad_null_appeals_t3"
      },
      "status": 400,
      "response": {
        "error": "invalid_text",
        "message": "text must be a string."
      },
      "new_log_entries": [
        {
          "event": "rejected",
          "status": "rejected",
          "reason": "invalid_text"
        }
      ],
      "passed": true
    },
    {
      "sent": {
        "text": "",
        "creator_id": "eval_bad_empty_appeals_t3"
      },
      "status": 400,
      "response": {
        "error": "empty_text",
        "message": "text is empty."
      },
      "new_log_entries": [
        {
          "event": "rejected",
          "status": "rejected",
          "reason": "empty_text"
        }
      ],
      "passed": true
    },
    {
      "sent": {
        "text": "   \t  ",
        "creator_id": "eval_bad_whitespace_appeals_t3"
      },
      "status": 400,
      "response": {
        "error": "empty_text",
        "message": "text is empty."
      },
      "new_log_entries": [
        {
          "event": "rejected",
          "status": "rejected",
          "reason": "empty_text"
        }
      ],
      "passed": true
    },
    {
      "sent": {
        "text": "<10005 chars>",
        "creator_id": "eval_bad_huge_appeals_t3"
      },
      "status": 400,
      "response": {
        "error": "text_too_long",
        "message": "text is longer than 10,000 characters."
      },
      "new_log_entries": [
        {
          "event": "rejected",
          "status": "rejected",
          "reason": "text_too_long"
        }
      ],
      "passed": true
    }
  ]
}
```
