from pyteal import *

def voting_contract():
    on_initialization = Seq([
        App.localPut(Int(0), Int(0)),  # Initialize the vote count (storage 0) to 0
        Return(Int(1))  # Return success
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