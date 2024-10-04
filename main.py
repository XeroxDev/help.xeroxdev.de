def define_env(env):
  @env.macro
  def badges(repo_owner="XeroxDev", repo="Loupedeck-plugin-YTMDesktop", forks=True, stars=True, watchers=True, contributors=True, issues=True, issues_closed=True, issues_pr=True,
             issues_pr_closed=True, prs_welcome=True, release=True, github_downloads=True, loupedeck=None, awesome_badges=True):
    """
    This command is used to render the default badges.
    """

    output = []
    if forks:
      output.append(f"[![Forks](https://img.shields.io/github/forks/{repo_owner}/{repo}?color=blue&style=for-the-badge)](https://github.com/{repo_owner}/{repo}/network/members)")
    if stars:
      output.append(f"[![Stars](https://img.shields.io/github/stars/{repo_owner}/{repo}?color=yellow&style=for-the-badge)](https://github.com/{repo_owner}/{repo}/stargazers)")
    if watchers:
      output.append(f"[![Watchers](https://img.shields.io/github/watchers/{repo_owner}/{repo}?color=lightgray&style=for-the-badge)](https://github.com/{repo_owner}/{repo}/watchers)")
    if contributors:
      output.append(f"[![Contributors](https://img.shields.io/github/contributors/{repo_owner}/{repo}?color=green&style=for-the-badge)](https://github.com/{repo_owner}/{repo}/graphs/contributors)")
    if issues:
      output.append(f"[![Issues](https://img.shields.io/github/issues/{repo_owner}/{repo}?color=yellow&style=for-the-badge)](https://github.com/{repo_owner}/{repo}/issues)")
    if issues_closed:
      output.append(
        f"[![Issues closed](https://img.shields.io/github/issues-closed/{repo_owner}/{repo}?color=yellow&style=for-the-badge)](https://github.com/{repo_owner}/{repo}/issues?q=is%3Aissue+is%3Aclosed)")
    if issues_pr:
      output.append(f"[![Issues-pr](https://img.shields.io/github/issues-pr/{repo_owner}/{repo}?color=yellow&style=for-the-badge)](https://github.com/{repo_owner}/{repo}/pulls)")
    if issues_pr_closed:
      output.append(
        f"[![Issues-pr closed](https://img.shields.io/github/issues-pr-closed/{repo_owner}/{repo}?color=yellow&style=for-the-badge)](https://github.com/{repo_owner}/{repo}/pulls?q=is%3Apr+is%3Aclosed)")
    if prs_welcome:
      output.append(f"[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](https://github.com/{repo_owner}/{repo}/compare)")
    if release:
      output.append(f"[![Release](https://img.shields.io/github/release/{repo_owner}/{repo}?color=black&style=for-the-badge)](https://github.com/{repo_owner}/{repo}/releases)")
    if github_downloads:
      output.append(
        f"[![GitHub Downloads](https://img.shields.io/github/downloads/{repo_owner}/{repo}/total.svg?color=CC2255&style=for-the-badge&logo=github)](https://github.com/{repo_owner}/{repo}/releases)")
    if loupedeck:
      output.append(
        f"[![Loupedeck Downloads](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Floupedeckmarketplace.com%2Fapi%2Fasset%2F{loupedeck}&query=%24.downloadCount&style=for-the-badge&logo=logitech&label=Downloads&color=00bbbb)](https://loupedeckmarketplace.com/asset/{loupedeck})")
    if awesome_badges:
      output.append(f"[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green?style=for-the-badge)](https://shields.io)")

    # split them into rows of 3, and due to markdown, it has to be double newlines
    return "\n\n".join([" ".join(output[i:i + 3]) for i in range(0, len(output), 3)])

  @env.macro
  def links_section(repo="Loupedeck-plugin-YTMDesktop", download=None, loupedeck=None, source=True, changelog=True, repo_owner="XeroxDev"):
    """
    This command is used to render a default links section.
    """
    output = []
    if download:
      output.append(f"[Download :material-download:](https://github.com/{repo_owner}/{repo}/releases/latest/download/{download}){{: .md-button .md-button--success }}")
    if source:
      output.append(f"[Source Code :material-source-branch:](https://github.com/{repo_owner}/{repo}/){{: .md-button }}")
    if changelog:
      output.append(f"[Changelog :material-text-long:](https://github.com/{repo_owner}/{repo}/blob/master/CHANGELOG.md){{: .md-button .md-button--info }}")
    if loupedeck:
      output.append(f"[Loupedeck Marketplace :material-store:](https://loupedeckmarketplace.com/asset/{loupedeck}){{: .md-button .md-button--light }}")
    return "\n".join(output)

  @env.macro
  def feedback_section(repo=None, repo_owner="XeroxDev"):
    """
    This command is used to render a default feedback section. The Github link is optional.
    """
    output = [
      f"Do you have any issues, a question or just want to give feedback?",
      f"",
      f"Please feel free to join my Discord and ask me there or open an issue on GitHub. I will try to help you as soon as possible.",
      f"",
      f"[Discord :fontawesome-brands-discord:](https://x.xeroxdev.de/s/discord){{: .md-button .md-button--success }}"
    ]
    if repo:
      output.append(f"[GitHub :material-github:](https://github.com/{repo_owner}/{repo}/issues/new/choose){{: .md-button .md-button--light }}")
    return "\n".join(output)
