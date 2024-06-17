{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-24.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in
      {
        devShells.${system}.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            # Nix env
            nil
            nixpkgs-fmt

            # C env
            stdenv.cc

            # Python
            python310
            python310Packages.pip
          ];

          shellHook = with pkgs; ''
            export LD_LIBRARY_PATH="${stdenv.cc.cc.lib}/lib"
            source .venv/bin/activate
          '';
        };
      };
}
