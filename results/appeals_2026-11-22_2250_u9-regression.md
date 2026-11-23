# Appeal path and bad-input log check — u9-regression

- Produced by: `run_appeals.py::run_trial`
- Service: `app.py::appeal`, `app.py::submit`
- 3 trials · 2026-11-22 22:50

## Trial 1

```json
{
  "appeals": [
    {
      "content_id": "772de821-bb85-45c9-bafa-f7ad5bd76a1c",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "772de821-bb85-45c9-bafa-f7ad5bd76a1c",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "1d09a4c1-43eb-4065-8818-b81f088562cd",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "1d09a4c1-43eb-4065-8818-b81f088562cd",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "1ae75e11-2708-4340-9187-7bc5fe3eb3f3",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "1ae75e11-2708-4340-9187-7bc5fe3eb3f3",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "c11cf1ee-0030-460e-8ddf-c18e1a99b40a",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "c11cf1ee-0030-460e-8ddf-c18e1a99b40a",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "d6a330be-7f0a-477f-9507-de911b327981",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "d6a330be-7f0a-477f-9507-de911b327981",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "f71b6b29-d433-4695-97cd-cb7253664bf5",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "f71b6b29-d433-4695-97cd-cb7253664bf5",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "79551c58-095e-4bff-a1f1-43aa4c103ab4",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "79551c58-095e-4bff-a1f1-43aa4c103ab4",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "8dfb3b5d-30f3-4e0a-ac47-abfbef2b0ab2",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "8dfb3b5d-30f3-4e0a-ac47-abfbef2b0ab2",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "4382531b-b41a-43e2-b7ba-2227da389cda",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "4382531b-b41a-43e2-b7ba-2227da389cda",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "f0e1ca52-bf16-4895-9fb6-44b744ed1cbb",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "f0e1ca52-bf16-4895-9fb6-44b744ed1cbb",
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
      "content_id": "a0235901-3a99-4033-b627-fa5a79963179",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "a0235901-3a99-4033-b627-fa5a79963179",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "aee0063d-1c65-49de-bc9f-23f39716f22f",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "aee0063d-1c65-49de-bc9f-23f39716f22f",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "4a6b7ef1-bcf7-411c-bc51-3e383528c425",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "4a6b7ef1-bcf7-411c-bc51-3e383528c425",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "c1a6583e-dba6-4f2c-bcd6-65ad48097bf7",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "c1a6583e-dba6-4f2c-bcd6-65ad48097bf7",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "691e5ae6-f38c-48b1-9ebb-a452a216362b",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "691e5ae6-f38c-48b1-9ebb-a452a216362b",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "bae12d33-cde3-4331-bc59-f7ab49c2a579",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "bae12d33-cde3-4331-bc59-f7ab49c2a579",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "73974fd2-4c40-44b4-92b2-0125c687d729",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "73974fd2-4c40-44b4-92b2-0125c687d729",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "4b892ab5-caa7-46c7-9c1e-3b6f326b7d7a",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "4b892ab5-caa7-46c7-9c1e-3b6f326b7d7a",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "a9280659-ffcb-46fb-8bb2-fa310ea9f891",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "a9280659-ffcb-46fb-8bb2-fa310ea9f891",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "303961c7-fbad-4162-83e4-2e436ef1b892",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "303961c7-fbad-4162-83e4-2e436ef1b892",
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
      "content_id": "e4f40e4d-d54a-4b7a-8137-e32c4aa9a50c",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "e4f40e4d-d54a-4b7a-8137-e32c4aa9a50c",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "67aa8103-e5b2-4ef4-9cf7-ebbd52420fd5",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "67aa8103-e5b2-4ef4-9cf7-ebbd52420fd5",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "14fbc106-c7e9-45a3-9deb-794ca1b1a81c",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "14fbc106-c7e9-45a3-9deb-794ca1b1a81c",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "f3a636b5-c093-45f2-a85e-81e01e33c255",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "f3a636b5-c093-45f2-a85e-81e01e33c255",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "c07934fb-e30c-487b-9829-5cf7e014ee24",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "c07934fb-e30c-487b-9829-5cf7e014ee24",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "ff89093a-ec27-4c1b-9e4b-ce08c86494f5",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "ff89093a-ec27-4c1b-9e4b-ce08c86494f5",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "2a330b33-604c-4cd9-8f87-02f94bce22e8",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "2a330b33-604c-4cd9-8f87-02f94bce22e8",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "56c3e2d0-98b4-4240-98be-06439ff5fe1d",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "56c3e2d0-98b4-4240-98be-06439ff5fe1d",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "b3027ea3-97fb-4bca-bfaa-b9ebd33baab2",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "b3027ea3-97fb-4bca-bfaa-b9ebd33baab2",
        "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
        "status": "under_review"
      },
      "appeal_entries_in_log": 1,
      "passed": true
    },
    {
      "content_id": "575b7d42-8a93-45bd-9786-f9d0b3b077d6",
      "submit_status": 200,
      "appeal_status": 200,
      "appeal_response": {
        "content_id": "575b7d42-8a93-45bd-9786-f9d0b3b077d6",
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
