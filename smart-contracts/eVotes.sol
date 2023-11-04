contract eVotes {

    mapping(address => Candidate) public candidateVotes;
    mapping(address => Voter) public voters;
    address public owner;

    struct Candidate {
        bool isValid;
        uint256 votes;
    }

    struct Voter {
        bool isRegistered;
        bool hasVoted;
    }

    modifier onlyOwner(address who) {
        require(owner == who, "You are not the owner");
        _;
    }

    constructor(address _owner) {
        owner = _owner;
    }

    function vote(address candidate) external {
        require(voters[msg.sender].isRegistered && !voters[msg.sender].hasVoted,
         "You already voted");
        require(candidateVotes[candidate].isValid, "That candidate is not valid");
        candidateVotes[candidate].votes++;
        voters[msg.sender].hasVoted = true;
    }

    function addUser(address user) public onlyOwner(msg.sender)  {
        voters[user].isRegistered = true;
    }

    function addCandidate(address user) external onlyOwner(msg.sender) {
        candidateVotes[user].isValid = true;
        addUser(user);
    }
}