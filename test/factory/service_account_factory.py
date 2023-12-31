import factory

from spaceone.core import utils
from spaceone.identity.model.service_account_model import ServiceAccount
from test.factory.project_factory import ProjectFactory


class ServiceAccountFactory(factory.mongoengine.MongoEngineFactory):

    class Meta:
        model = ServiceAccount

    service_account_id = factory.LazyAttribute(lambda o: utils.generate_id('sa'))
    service_account_type = 'GENERAL'
    trusted_service_account_id = None
    name = factory.LazyAttribute(lambda o: utils.random_string())
    data = {
        'account_id': '00123456'
    }
    provider = 'aws'
    project = factory.SubFactory(ProjectFactory)
    project_id = factory.LazyAttribute(lambda o: utils.generate_id('project'))
    tags = {'tag_key': 'tag_value'}
    domain_id = utils.generate_id('domain')
    created_at = factory.Faker('date_time')
