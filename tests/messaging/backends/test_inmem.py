import pytest
import uuid
from iceqube.common.six.moves.queue import Empty
from iceqube.messaging.backends import inmem
from iceqube.messaging.classes import Message, MessageType

MAILBOX = "pytesting"


@pytest.fixture
def defaultbackend():
    b = inmem.MessagingBackend()
    yield b


@pytest.fixture(params=[MessageType.START_JOB, MessageType.CANCEL_JOB])
def msg(request):
    m = Message(request.param, uuid.uuid4().hex)
    yield m


class TestBackend:
    def test_can_send_and_read_to_the_same_mailbox(self, defaultbackend, msg):
        defaultbackend.send(MAILBOX, msg)

        newmsg = defaultbackend.pop(MAILBOX)

        assert newmsg.type == msg.type
        assert newmsg.job_id == msg.job_id

    def test_new_instance_can_send_and_read_to_the_same_mailbox(self, defaultbackend, msg):
        defaultbackend.send(MAILBOX, msg)

        otherbackend = inmem.MessagingBackend()

        newmsg = otherbackend.pop(MAILBOX)

        assert newmsg.type == msg.type
        assert newmsg.job_id == msg.job_id

    def test_pop_raise_empty_when_no_messages(self, defaultbackend):

        with pytest.raises(Empty):
            defaultbackend.pop(MAILBOX)

    def test_popn_return_empty_list_when_no_messages(self, defaultbackend):
        msgs = defaultbackend.popn(MAILBOX)

        assert len(msgs) == 0
        assert type(msgs) == list
