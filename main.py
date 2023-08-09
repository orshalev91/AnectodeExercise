from evidences.base_evidence import Evidence
from evidences.post_evidence import PostEvidence
from evidences.user_evidence import UserEvidence
from helpers import *


if __name__ == "__main__":
    if check_connectivity(Evidence.base_url, Evidence.token):
        evidences = [UserEvidence(), PostEvidence()]
        for evidence in evidences:
            curr_evidence_result = evidence.fetch_evidence()
            if not curr_evidence_result is None:
                dump_json_file(f"{evidence.name}.json", curr_evidence_result)
