from input_output.input import get_yes_no_answer


def check_recovery_start(mps_to_recover, configured_mps=None):
    """
    Present the media packages about to be recovered to the user and ask whether a recovery should be attempted under
    these circumstances.

    :param mps_to_recover: The media packages that can be recovered.
    :type mps_to_recover: list
    :param configured_mps: The configured media packages to recover, if any.
    :type configured_mps: list
    :return: Whether the recovery should be started.
    :rtype: bool
    """

    print()
    print("The following {} media packages can be recovered:".format(len(mps_to_recover)))
    print("Media package                        | Version | Path")

    for mp in mps_to_recover:
        print("%36s | %7s | %s" % (mp.id, mp.version, mp.path))
    print()

    if configured_mps and len(configured_mps) > len(mps_to_recover):
        print("{} media packages cannot be recovered.\n".format((len(configured_mps) - len(mps_to_recover))))

    start_recover = get_yes_no_answer("Start recovery?")

    return start_recover
