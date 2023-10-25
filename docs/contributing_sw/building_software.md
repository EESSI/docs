# Building software (maintainers)

### Instructing the bot to build :hammer: { #bot_build }

Once the pull request is open, you can instruct the [bot :robot:](../bot.md) to build the software by posting a comment.

For more information, see the [building section in the bot documentation](../bot.md#building).

!!! warning
    Permission to trigger building of software must be granted to your GitHub account first!

    See [bot permissions](../bot.md#permissions) for more information.

#### Guidelines

* It may be wise to let the bot perform a test build first, rather than letting it build for a wide range
  of CPU targets.

* If one of the builds failed, you can let the bot retry that specific build.

* Make sure that the software has been built correctly for all [CPU targets](../software_layer/cpu_targets.md) before you deploy!

#### Checking the builds :mag:

If all goes well, you should see `SUCCESS` :grin: for each build, along with button :arrow_down_small:
to get more information about the checks that were performed, and metadata information on the resulting
artefact :package:.

!!! note
    **Make sure the result is what you expect it to be for all builds before you deploy!**

#### Failing builds :no_entry:

!!! warning
    The bot will currently not give you any information on how or why a build is failing.

    Ask for help in the `#software-layer` channel of the EESSI Slack if needed!

### Instructing the bot to deploy :rocket:

To make the [bot :robot:](../bot.md) deploy the successfully built software, you should
issue the corresponding instruction to the bot.

For more information, see the [deploying section in the bot documentation](../bot.md#deploying).

!!! warning
    Permission to trigger deployment of software installations must be granted to your GitHub account first!

    See [bot permissions](../bot.md#permissions) for more information.

### Merging the pull request

You should be able to verify in the pull request that the ingestion has been done,
since the CI should fail :x: initially to indicate that some software installations listed in
your modified easystack are missing.

Once the ingestion has been done, simply re-triggering the CI workflow should be sufficient to make it pass
:white_check_mark:, and then the pull request can be merged.

!!! note
    This assumes that the easystack file being modified is considered by the CI workflow file
    (`.github/workflows/test_eessi.yml`) that checks for missing installations, in the correct branch (for example
    `2023.06`) of the [software-layer](https://github.com/EESSI/software-layer).

    If that's not the case yet, update this workflow in your pull request as well to add the missing easystack file!

!!! warning
    You need permissions to re-trigger CI workflows and merge pull requests
    in the [software-layer](https://github.com/EESSI/software-layer) repository.

    Ask for help in the `#software-layer` channel of the EESSI Slack if needed!

### Getting help

If you have any questions, or if you need help with something, don't hesitate to contact us via
the `#software-layer` channel of the EESSI Slack.
