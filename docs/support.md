# Getting support for EESSI

<p align="center">
  <img width="40%" src="../img/logos/multixscale_logo.png" alt="MustiXscale logo">
</p>

Thanks to the [MultiXscale EuroHPC project](https://www.multixscale.eu) we are able to provide support to the users of EESSI. 

The **EESSI support portal** is hosted in GitLab: <https://gitlab.com/eessi/support>.

## How to report a problem or ask a question { #open-issue }

We recommend you to use a [GitLab account](https://gitlab.com/users/sign_in) if you want to get help from the EESSI support team.

If you have a GitLab account you can submit your problems or questions on 
EESSI via the issue tracker of the EESSI support portal at <https://gitlab.com/eessi/support/-/issues>.
Please use one of the provided templates (report a problem, software request, question, ...) when creating an issue.

You can also contact us via our e-mail address `support (@) eessi.io`, which will automatically create a (private) issue in the EESSI support portal.
When you send us an email, please provide us with as much information as possible on your question or problem.
You can find an overview of the information that we would like to receive in the [README of the EESSI support portal](https://gitlab.com/eessi/support/-/blob/main/README.md).

## Level of Support

We provide support for EESSI according to a "reasonable effort" standard. That means we will go into reasonable effort to help you, but we may not have the time to explore every potential cause, and it may not lead to a (quick) solution. You can compare this to the level of support you typically get from other _active_ open source projects.

Note that the more complete your reported issue is (e.g. description of the error, what you ran, the software environment in which you ran, minimal reproducer, etc.) the bigger the chance is that we can help you with "reasonable effort".

### What do we provide support for

#### Accessing and using the EESSI software stack

If you have trouble connecting to the software stack, such as trouble related to installing or configuring CernVM-FS to access the [EESSI filesystem layer](filesystem_layer.md), or running the software installations included in the EESSI [compatibility layer](compatibility_layer.md) or [software layer](software_layer.md), please [contact us](#open-issue).

Note that we can only help with problems related to the software *installations* (getting the software to run, to perform as expected, etc.). We *do not* provide support for using specific features of the provided software, nor can we fix (known or unknown) bugs in the software included in EESSI. We can only help with diagnosing and fixing problems that are caused by *how* the software was built and installed in EESSI.

#### Software requests

We are open to software requests for software that is not included in EESSI yet.

The quickest way to add additional software to EESSI is by contributing it yourself as a community contribution, please see the [documentation on adding software](contributing_sw/adding_software.md).

Alternatively, you can send in a request to our support team. Please try to provide as much information on the software as possible: preferably use the [issue template](https://gitlab.com/eessi/support/-/issues/new?issuable_template=Software_request) (which requires you to log in to GitLab), or make sure to cover the items listed [here](https://gitlab.com/eessi/support/-/blob/main/.gitlab/issue_templates/Software_request.md).

Be aware that we can only provide software that has an appropriate open source license.

#### EESSI test suite

If you are using the [EESSI test suite](https://github.com/EESSI/test-suite), you can get help via the [EESSI support portal](#open-issue).

#### Build-and-deploy bot

If you are using the [EESSI build-and-deploy bot](https://github.com/EESSI/eessi-bot-software-layer), you can get help via the [EESSI support portal](#open-issue).


### What do we *not* provide support for

Do not contact the EESSI support team to get help with *using* software that is included in EESSI, unless you think the problems you are seeing are related to *how* the software was built and installed.

Please consult the documentation of the software you are using, or contact the developers of the software directly, if you have questions regarding using the software, or if you think you have found a bug.
