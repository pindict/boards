# PinDict Boards

Remote board / sensor / snippet database for the [PinDict](https://github.com/pindict) Flutter app.

## Layout

- `manifest.json` — version, file list with SHA1 (consumed by the app)
- `manifest.yaml` — same content in YAML for hand editing
- `boards/*.yaml` — per-board pinout definitions
- `sensors/*.yaml` — sensor definitions
- `snippets/*.yaml` — code snippets

## Updating

1. Edit YAML files (or add new ones in `boards/` / `sensors/` / `snippets/`)
2. Add the filename to `manifest.yaml`
3. Bump the `version` in `manifest.yaml`
4. Regenerate the JSON manifest:

   ```
   python3 scripts/gen_manifest.py
   ```

5. Commit and push. The app refreshes via raw.githubusercontent.com.

## License

Content under CC BY 4.0. Schema and scripts under MIT.
