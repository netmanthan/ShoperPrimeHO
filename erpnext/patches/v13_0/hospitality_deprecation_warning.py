import click


def execute():

	click.secho(
		"Hospitality domain is moved to a separate app and will be removed from ShoperPrime HO in version-14.\n"
		"When upgrading to ShoperPrime HO version-14, please install the app to continue using the Hospitality domain: https://github.com/frappe/hospitality",
		fg="yellow",
	)
