from pyteal import *

def voting_contract():
    program = Gtxn[1].type_enum() == TxnType.Payment    
    SENDER = txn.sender()`
    RECEIVER = txn.Receiver()
    can_vote_key = Bytes('canVote')
    votes_key = Bytes('votes')
    on_initialization = Seq([
        App.localPut(SENDER, can_vote_key, Int(0)),
        acc_votes := App.localGet(RECEIVER, votes_key),
        App.localPut(RECEIVER, votes_key, acc_votes + Int(1)),
        Return(Int(0))
    ])

    on_vote = Seq([
        App.localPut(Int(0), Add(App.localGet(Int(0), Int(0)), Int(1))),  # Increment the vote count
        Return(Int(1))  # Return success
    ])

    program = Cond(
        [Txn.application_id() == Int(0), on_initialization],  # Initialize the contract
        [Txn.application_id() != Int(0), on_vote]  # Voting
    )

    return program

if __name__ == "__main__":
    compiled = compileTeal(voting_contract(), mode=Mode.Application)
    with open("compiled_voting_contract.teal", "w") as f:
        f.write(compiled)